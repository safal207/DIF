#!/usr/bin/env python3
"""Validate Agent Selection Receipts and their human authorization pairs."""

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
HUMAN_VALIDATOR_PATH = TOOLS_DIR / "validate_human_response.py"

_human_spec = importlib.util.spec_from_file_location(
    "dif_validate_human_response", HUMAN_VALIDATOR_PATH
)
if _human_spec is None or _human_spec.loader is None:
    raise RuntimeError("cannot load Human Response Receipt validator")
human_validator = importlib.util.module_from_spec(_human_spec)
_human_spec.loader.exec_module(human_validator)

PAIR_FIELDS = {"authorization", "selection"}
SELECTION_REQUIRED_FIELDS = {
    "schema_version",
    "selection_id",
    "question_id",
    "selected_option",
    "decision_source",
    "authorization_response_id",
    "selected_at",
}
SELECTION_OPTIONAL_FIELDS = {"session_id", "rationale", "metadata"}
SELECTION_ALLOWED_FIELDS = SELECTION_REQUIRED_FIELDS | SELECTION_OPTIONAL_FIELDS


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


def validate_selection_receipt(receipt: Any) -> list[str]:
    """Validate the standalone Agent Selection Receipt shape and semantics."""

    if not isinstance(receipt, dict):
        return ["selection must be a JSON object"]

    errors: list[str] = []
    missing = sorted(SELECTION_REQUIRED_FIELDS - receipt.keys())
    unexpected = sorted(receipt.keys() - SELECTION_ALLOWED_FIELDS)
    if missing:
        errors.append(f"selection missing required fields: {', '.join(missing)}")
    if unexpected:
        errors.append(f"selection has unexpected fields: {', '.join(unexpected)}")
    if missing:
        return errors

    if receipt["schema_version"] != SCHEMA_VERSION:
        errors.append(
            f"selection schema_version must be {SCHEMA_VERSION!r}, "
            f"got {receipt['schema_version']!r}"
        )

    for field in (
        "selection_id",
        "question_id",
        "selected_option",
        "authorization_response_id",
    ):
        if not _non_empty_string(receipt[field]):
            errors.append(f"selection {field} must be a non-empty string")

    if receipt["decision_source"] != "AGENT":
        errors.append("selection decision_source must be AGENT")

    if parse_rfc3339(receipt["selected_at"]) is None:
        errors.append(
            "selection selected_at must be a timezone-aware RFC3339 timestamp"
        )

    for field in ("session_id", "rationale"):
        value = receipt.get(field)
        if value is not None and not _non_empty_string(value):
            errors.append(f"selection {field} must be null or a non-empty string")

    metadata = receipt.get("metadata")
    if metadata is not None and not isinstance(metadata, dict):
        errors.append("selection metadata must be an object when provided")

    return errors


def validate_pair_document(document: Any) -> list[str]:
    """Validate an authorization/selection fixture as one linked event pair."""

    if not isinstance(document, dict):
        return ["pair document must be a JSON object"]

    errors: list[str] = []
    missing = sorted(PAIR_FIELDS - document.keys())
    unexpected = sorted(document.keys() - PAIR_FIELDS)
    if missing:
        errors.append(f"pair missing fields: {', '.join(missing)}")
    if unexpected:
        errors.append(f"pair has unexpected fields: {', '.join(unexpected)}")
    if missing:
        return errors

    authorization = document["authorization"]
    selection = document["selection"]

    authorization_errors = human_validator.validate_receipt(authorization)
    errors.extend(f"authorization: {error}" for error in authorization_errors)
    selection_errors = validate_selection_receipt(selection)
    errors.extend(selection_errors)

    if not isinstance(authorization, dict) or not isinstance(selection, dict):
        return errors

    response_id = authorization.get("response_id")
    if not _non_empty_string(response_id):
        errors.append(
            "authorization response_id is required for an agent selection link"
        )
    elif selection.get("authorization_response_id") != response_id:
        errors.append(
            "selection authorization_response_id does not match authorization response_id"
        )

    if selection.get("question_id") != authorization.get("question_id"):
        errors.append("selection and authorization question_id values must match")

    if authorization.get("response_state") != "DELEGATED_TO_AGENT":
        errors.append(
            "authorization response_state must be DELEGATED_TO_AGENT"
        )
    if authorization.get("decision_source") != "HUMAN":
        errors.append("authorization decision_source must be HUMAN")
    if authorization.get("human_confirmed") is not True:
        errors.append("authorization must be human_confirmed")
    if authorization.get("agent_authority") != "CHOOSE":
        errors.append("authorization agent_authority must be CHOOSE")
    if authorization.get("selected_option") is not None:
        errors.append(
            "authorization selected_option must remain null; the agent choice belongs in selection"
        )

    authorization_time = parse_rfc3339(authorization.get("observed_at"))
    selection_time = parse_rfc3339(selection.get("selected_at"))
    if (
        authorization_time is not None
        and selection_time is not None
        and selection_time < authorization_time
    ):
        errors.append("selection selected_at cannot precede authorization observed_at")

    authorization_session = authorization.get("session_id")
    selection_session = selection.get("session_id")
    if (
        authorization_session is not None
        and selection_session is not None
        and authorization_session != selection_session
    ):
        errors.append("selection and authorization session_id values must match")

    return errors


def validate_path(path: Path) -> list[str]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read valid JSON: {exc}"]
    return validate_pair_document(document)


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
        description="Validate Agent Selection Receipt authorization pairs."
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
