#!/usr/bin/env python3
"""Validate DIF Human Response Receipt semantic invariants."""

from __future__ import annotations

import argparse
import glob
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1"

STATE_RULES: dict[str, dict[str, Any]] = {
    "PENDING": {
        "source": "SYSTEM",
        "interaction": False,
        "confirmed": False,
        "authority": "STOP_AND_WAIT",
        "selection": "forbidden",
    },
    "ANSWERED_BY_USER": {
        "source": "HUMAN",
        "interaction": True,
        "confirmed": True,
        "authority": "CONTINUE",
        "selection": "required",
    },
    "DECLINED_OPTIONS": {
        "source": "HUMAN",
        "interaction": True,
        "confirmed": False,
        "authority": "ASK_FOLLOWUP",
        "selection": "forbidden",
    },
    "DEFERRED_BY_USER": {
        "source": "HUMAN",
        "interaction": True,
        "confirmed": False,
        "authority": "STOP_AND_WAIT",
        "selection": "forbidden",
    },
    "DELEGATED_TO_AGENT": {
        "source": "HUMAN",
        "interaction": True,
        "confirmed": True,
        "authority": "CHOOSE",
        "selection": "forbidden",
    },
    "TIMED_OUT": {
        "source": "SYSTEM",
        "interaction": False,
        "confirmed": False,
        "authority": "STOP_AND_WAIT",
        "selection": "forbidden",
    },
    "DISMISSED": {
        "source": "HUMAN",
        "interaction": True,
        "confirmed": False,
        "authority": "STOP_AND_WAIT",
        "selection": "forbidden",
    },
    "CONNECTION_LOST": {
        "source": "TRANSPORT",
        "interaction": False,
        "confirmed": False,
        "authority": "STOP_AND_WAIT",
        "selection": "forbidden",
    },
    "CANCELLED_BY_SYSTEM": {
        "source": "SYSTEM",
        "interaction": False,
        "confirmed": False,
        "authority": "STOP_AND_WAIT",
        "selection": "forbidden",
    },
}

REQUIRED_FIELDS = {
    "schema_version",
    "question_id",
    "response_state",
    "selected_option",
    "decision_source",
    "human_interaction_observed",
    "human_confirmed",
    "agent_authority",
    "observed_at",
}
OPTIONAL_FIELDS = {
    "response_id",
    "session_id",
    "transport_id",
    "metadata",
}
ALLOWED_FIELDS = REQUIRED_FIELDS | OPTIONAL_FIELDS


def parse_rfc3339(value: Any) -> datetime | None:
    """Parse a timezone-aware RFC3339 value, accepting Z or an offset."""

    if not isinstance(value, str) or "T" not in value:
        return None
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def is_rfc3339_timestamp(value: Any) -> bool:
    return parse_rfc3339(value) is not None


def _validate_optional_id(receipt: dict[str, Any], field: str) -> list[str]:
    value = receipt.get(field)
    if value is None:
        return []
    if not isinstance(value, str) or not value.strip():
        return [f"{field} must be null or a non-empty string"]
    return []


def validate_receipt(receipt: Any) -> list[str]:
    """Return semantic validation errors for one receipt."""

    if not isinstance(receipt, dict):
        return ["receipt must be a JSON object"]

    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - receipt.keys())
    unexpected = sorted(receipt.keys() - ALLOWED_FIELDS)
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")
    if unexpected:
        errors.append(f"unexpected fields: {', '.join(unexpected)}")
    if missing:
        return errors

    if receipt["schema_version"] != SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SCHEMA_VERSION!r}, "
            f"got {receipt['schema_version']!r}"
        )

    if not isinstance(receipt["question_id"], str) or not receipt[
        "question_id"
    ].strip():
        errors.append("question_id must be a non-empty string")

    if not is_rfc3339_timestamp(receipt["observed_at"]):
        errors.append(
            "observed_at must be a timezone-aware RFC3339 timestamp "
            "using Z or an explicit UTC offset"
        )

    for field in ("response_id", "session_id", "transport_id"):
        errors.extend(_validate_optional_id(receipt, field))

    metadata = receipt.get("metadata")
    if metadata is not None and not isinstance(metadata, dict):
        errors.append("metadata must be an object when provided")

    state = receipt["response_state"]
    rule = STATE_RULES.get(state)
    if rule is None:
        errors.append(f"unknown response_state: {state!r}")
        return errors

    if receipt["decision_source"] != rule["source"]:
        errors.append(
            f"{state} requires decision_source={rule['source']}, "
            f"got {receipt['decision_source']!r}"
        )
    if receipt["human_interaction_observed"] is not rule["interaction"]:
        errors.append(
            f"{state} requires human_interaction_observed="
            f"{rule['interaction']}"
        )
    if receipt["human_confirmed"] is not rule["confirmed"]:
        errors.append(f"{state} requires human_confirmed={rule['confirmed']}")
    if receipt["agent_authority"] != rule["authority"]:
        errors.append(
            f"{state} requires agent_authority={rule['authority']}, "
            f"got {receipt['agent_authority']!r}"
        )

    selected = receipt["selected_option"]
    if rule["selection"] == "required":
        if not isinstance(selected, str) or not selected.strip():
            errors.append(f"{state} requires a non-empty selected_option")
    elif selected is not None:
        errors.append(f"{state} forbids selected_option")

    if receipt["human_confirmed"] is False and receipt["agent_authority"] in {
        "CONTINUE",
        "CHOOSE",
    }:
        errors.append(
            "unconfirmed human response cannot grant CONTINUE or CHOOSE authority"
        )
    if receipt["decision_source"] in {"SYSTEM", "TRANSPORT"} and receipt[
        "human_confirmed"
    ]:
        errors.append(
            "SYSTEM or TRANSPORT decision_source cannot be human_confirmed"
        )

    return errors


def validate_path(path: Path) -> list[str]:
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read valid JSON: {exc}"]
    return validate_receipt(receipt)


def expand_path_args(path_args: list[str]) -> tuple[list[Path], list[str]]:
    """Expand CLI glob arguments consistently across operating systems."""

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
        description="Validate DIF Human Response Receipt files."
    )
    parser.add_argument("paths", nargs="+")
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit one machine-readable result array",
    )
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
