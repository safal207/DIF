#!/usr/bin/env python3
"""Validate Human → Agent Selection → Action Execution receipt chains."""

from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1"
TOOLS_DIR = Path(__file__).resolve().parent
SELECTION_VALIDATOR_PATH = TOOLS_DIR / "validate_agent_selection.py"

_selection_spec = importlib.util.spec_from_file_location(
    "dif_validate_agent_selection", SELECTION_VALIDATOR_PATH
)
if _selection_spec is None or _selection_spec.loader is None:
    raise RuntimeError("cannot load Agent Selection Receipt validator")
selection_validator = importlib.util.module_from_spec(_selection_spec)
_selection_spec.loader.exec_module(selection_validator)

CHAIN_FIELDS = {"authorization", "selection", "execution"}
EXECUTION_REQUIRED_FIELDS = {
    "schema_version",
    "execution_id",
    "question_id",
    "selection_id",
    "selected_option",
    "action_type",
    "action_target",
    "action_parameters",
    "initiated_by",
    "executed_by",
    "execution_status",
    "started_at",
    "completed_at",
    "error",
}
EXECUTION_OPTIONAL_FIELDS = {
    "session_id",
    "idempotency_key",
    "result",
    "metadata",
}
EXECUTION_ALLOWED_FIELDS = EXECUTION_REQUIRED_FIELDS | EXECUTION_OPTIONAL_FIELDS
EXECUTORS = {"AGENT", "TOOL", "SYSTEM"}
EXECUTION_STATUSES = {"SUCCEEDED", "FAILED"}


def parse_rfc3339(value: Any) -> datetime | None:
    if not isinstance(value, str) or "T" not in value:
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def json_values_exactly_equal(left: Any, right: Any) -> bool:
    """Compare JSON values canonically without Python's bool/number coercion.

    Python considers ``True == 1`` and ``1 == 1.0``. Canonical JSON encoding
    preserves those distinctions while ignoring object key order.
    """

    try:
        left_json = json.dumps(
            left,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        )
        right_json = json.dumps(
            right,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        )
    except (TypeError, ValueError):
        return False
    return left_json == right_json


def validate_execution_receipt(receipt: Any) -> list[str]:
    """Validate the standalone Action Execution Receipt."""

    if not isinstance(receipt, dict):
        return ["execution must be a JSON object"]

    errors: list[str] = []
    missing = sorted(EXECUTION_REQUIRED_FIELDS - receipt.keys())
    unexpected = sorted(receipt.keys() - EXECUTION_ALLOWED_FIELDS)
    if missing:
        errors.append(f"execution missing required fields: {', '.join(missing)}")
    if unexpected:
        errors.append(f"execution has unexpected fields: {', '.join(unexpected)}")
    if missing:
        return errors

    if receipt["schema_version"] != SCHEMA_VERSION:
        errors.append(
            f"execution schema_version must be {SCHEMA_VERSION!r}, "
            f"got {receipt['schema_version']!r}"
        )

    for field in (
        "execution_id",
        "question_id",
        "selection_id",
        "selected_option",
        "action_type",
        "action_target",
    ):
        if not _non_empty_string(receipt[field]):
            errors.append(f"execution {field} must be a non-empty string")

    if not isinstance(receipt["action_parameters"], dict):
        errors.append("execution action_parameters must be an object")
    if receipt["initiated_by"] != "AGENT":
        errors.append("execution initiated_by must be AGENT")
    if receipt["executed_by"] not in EXECUTORS:
        errors.append("execution executed_by must be AGENT, TOOL, or SYSTEM")
    if receipt["execution_status"] not in EXECUTION_STATUSES:
        errors.append("execution execution_status must be SUCCEEDED or FAILED")

    started_at = parse_rfc3339(receipt["started_at"])
    completed_at = parse_rfc3339(receipt["completed_at"])
    if started_at is None:
        errors.append("execution started_at must be a timezone-aware RFC3339 timestamp")
    if completed_at is None:
        errors.append(
            "execution completed_at must be a timezone-aware RFC3339 timestamp"
        )
    if started_at is not None and completed_at is not None and completed_at < started_at:
        errors.append("execution completed_at cannot precede started_at")

    error = receipt["error"]
    if receipt["execution_status"] == "SUCCEEDED" and error is not None:
        errors.append("successful execution must have error=null")
    if receipt["execution_status"] == "FAILED" and not _non_empty_string(error):
        errors.append("failed execution must include a non-empty error")

    for field in ("session_id", "idempotency_key"):
        value = receipt.get(field)
        if value is not None and not _non_empty_string(value):
            errors.append(f"execution {field} must be null or a non-empty string")
    for field in ("result", "metadata"):
        value = receipt.get(field)
        if value is not None and not isinstance(value, dict):
            errors.append(f"execution {field} must be an object when provided")
    return errors


def validate_chain_document(document: Any) -> list[str]:
    """Validate a complete authorization, selection, and execution chain."""

    if not isinstance(document, dict):
        return ["chain document must be a JSON object"]

    errors: list[str] = []
    missing = sorted(CHAIN_FIELDS - document.keys())
    unexpected = sorted(document.keys() - CHAIN_FIELDS)
    if missing:
        errors.append(f"chain missing fields: {', '.join(missing)}")
    if unexpected:
        errors.append(f"chain has unexpected fields: {', '.join(unexpected)}")
    if missing:
        return errors

    authorization = document["authorization"]
    selection = document["selection"]
    execution = document["execution"]

    pair_errors = selection_validator.validate_pair_document(
        {"authorization": authorization, "selection": selection}
    )
    errors.extend(f"selection pair: {error}" for error in pair_errors)
    errors.extend(validate_execution_receipt(execution))

    if not isinstance(selection, dict) or not isinstance(execution, dict):
        return errors

    contract = selection.get("action_contract")
    errors.extend(selection_validator.validate_action_contract(contract))
    if not isinstance(contract, dict):
        errors.append("selection action_contract is required for execution")
        return errors

    if execution.get("selection_id") != selection.get("selection_id"):
        errors.append("execution selection_id must match selection selection_id")
    if execution.get("question_id") != selection.get("question_id"):
        errors.append("execution question_id must match selection question_id")
    if execution.get("selected_option") != selection.get("selected_option"):
        errors.append("execution selected_option must match selection selected_option")
    if execution.get("action_type") != contract.get("action_type"):
        errors.append("execution action_type must match selection action_contract")
    if execution.get("action_target") != contract.get("action_target"):
        errors.append("execution action_target must match selection action_contract")
    if not json_values_exactly_equal(
        execution.get("action_parameters"), contract.get("parameters")
    ):
        errors.append(
            "execution action_parameters must exactly match selection action_contract"
        )

    selected_at = parse_rfc3339(selection.get("selected_at"))
    started_at = parse_rfc3339(execution.get("started_at"))
    if selected_at is not None and started_at is not None and started_at < selected_at:
        errors.append("execution started_at cannot precede selection selected_at")

    selection_session = selection.get("session_id")
    execution_session = execution.get("session_id")
    if (
        selection_session is not None
        and execution_session is not None
        and selection_session != execution_session
    ):
        errors.append("execution and selection session_id values must match")
    return errors


def validate_path(path: Path) -> list[str]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read valid JSON: {exc}"]
    return validate_chain_document(document)


def expand_path_args(path_args: list[str]) -> tuple[list[Path], list[str]]:
    expanded: list[Path] = []
    errors: list[str] = []
    seen: set[Path] = set()
    for raw_path in path_args:
        if glob.has_magic(raw_path):
            matches = sorted(Path(match) for match in glob.glob(raw_path))
            if not matches:
                errors.append(f"no files matched pattern: {raw_path}")
                continue
        else:
            matches = [Path(raw_path)]
        for path in matches:
            if path not in seen:
                seen.add(path)
                expanded.append(path)
    return expanded, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Human → Agent Selection → Action Execution chains."
    )
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    paths, expansion_errors = expand_path_args(args.paths)
    results = [
        {
            "path": error.removeprefix("no files matched pattern: "),
            "status": "INVALID",
            "errors": [error],
        }
        for error in expansion_errors
    ]
    failed = bool(expansion_errors)
    for path in paths:
        errors = validate_path(path)
        failed = failed or bool(errors)
        results.append(
            {
                "path": str(path),
                "status": "OK" if not errors else "INVALID",
                "errors": errors,
            }
        )

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            print(f"{result['status']}: {result['path']}")
            for error in result["errors"]:
                print(f"  - {error}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
