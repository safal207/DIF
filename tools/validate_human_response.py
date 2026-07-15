#!/usr/bin/env python3
"""Validate DIF Human Response Receipt semantic invariants.

This validator intentionally uses only the Python standard library so the
conformance fixtures can run in any basic CI environment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "0.1"
ISO_8601_UTC = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$"
)

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


def validate_receipt(receipt: Any) -> list[str]:
    """Return semantic validation errors for one receipt."""

    if not isinstance(receipt, dict):
        return ["receipt must be a JSON object"]

    errors: list[str] = []

    missing = sorted(REQUIRED_FIELDS - receipt.keys())
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")
        return errors

    if receipt["schema_version"] != SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SCHEMA_VERSION!r}, "
            f"got {receipt['schema_version']!r}"
        )

    question_id = receipt["question_id"]
    if not isinstance(question_id, str) or not question_id.strip():
        errors.append("question_id must be a non-empty string")

    observed_at = receipt["observed_at"]
    if not isinstance(observed_at, str) or not ISO_8601_UTC.match(observed_at):
        errors.append("observed_at must be an ISO-8601 UTC timestamp ending in Z")

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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate DIF Human Response Receipt files."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit one machine-readable result array",
    )
    args = parser.parse_args(argv)

    results = []
    failed = False
    for path in args.paths:
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
