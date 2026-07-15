from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "tools" / "validate_human_response.py"

spec = importlib.util.spec_from_file_location(
    "validate_human_response", VALIDATOR_PATH
)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class HumanResponseIntegrityTests(unittest.TestCase):
    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_all_valid_fixtures_pass(self) -> None:
        fixtures = sorted(
            (ROOT / "fixtures" / "human-response-state" / "valid").glob("*.json")
        )
        self.assertGreaterEqual(len(fixtures), 7)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                self.assertEqual([], validator.validate_receipt(self.load(fixture)))

    def test_all_invalid_fixtures_fail(self) -> None:
        fixtures = sorted(
            (ROOT / "fixtures" / "human-response-state" / "invalid").glob("*.json")
        )
        self.assertGreaterEqual(len(fixtures), 6)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                self.assertTrue(validator.validate_receipt(self.load(fixture)))

    def test_skip_is_not_delegation(self) -> None:
        receipt = self.load(
            ROOT
            / "fixtures"
            / "human-response-state"
            / "valid"
            / "skipped.json"
        )
        self.assertEqual("DECLINED_OPTIONS", receipt["response_state"])
        self.assertEqual("ASK_FOLLOWUP", receipt["agent_authority"])
        self.assertFalse(receipt["human_confirmed"])

    def test_timeout_never_selects_or_continues(self) -> None:
        receipt = self.load(
            ROOT
            / "fixtures"
            / "human-response-state"
            / "valid"
            / "timed-out.json"
        )
        self.assertIsNone(receipt["selected_option"])
        self.assertEqual("STOP_AND_WAIT", receipt["agent_authority"])
        self.assertFalse(receipt["human_confirmed"])

    def test_only_explicit_delegation_grants_choose(self) -> None:
        receipt = self.load(
            ROOT
            / "fixtures"
            / "human-response-state"
            / "valid"
            / "user-delegated.json"
        )
        self.assertEqual("DELEGATED_TO_AGENT", receipt["response_state"])
        self.assertEqual("HUMAN", receipt["decision_source"])
        self.assertTrue(receipt["human_interaction_observed"])
        self.assertTrue(receipt["human_confirmed"])
        self.assertEqual("CHOOSE", receipt["agent_authority"])

    def test_agent_selection_is_not_a_human_response_receipt(self) -> None:
        receipt = {
            "schema_version": "0.1",
            "question_id": "q-agent-selection",
            "response_state": "DELEGATED_TO_AGENT",
            "selected_option": "option-b",
            "decision_source": "AGENT",
            "human_interaction_observed": True,
            "human_confirmed": True,
            "agent_authority": "CHOOSE",
            "observed_at": "2026-07-15T20:00:00Z",
        }
        errors = validator.validate_receipt(receipt)
        self.assertTrue(any("decision_source=HUMAN" in error for error in errors))
        self.assertTrue(any("forbids selected_option" in error for error in errors))

    def test_rfc3339_offset_timestamp_is_accepted(self) -> None:
        receipt = self.load(
            ROOT
            / "fixtures"
            / "human-response-state"
            / "valid"
            / "offset-timestamp.json"
        )
        self.assertEqual([], validator.validate_receipt(receipt))

    def test_naive_timestamp_is_rejected(self) -> None:
        receipt = {
            "schema_version": "0.1",
            "question_id": "q-naive-time",
            "response_state": "TIMED_OUT",
            "selected_option": None,
            "decision_source": "SYSTEM",
            "human_interaction_observed": False,
            "human_confirmed": False,
            "agent_authority": "STOP_AND_WAIT",
            "observed_at": "2026-07-15T20:00:00",
        }
        errors = validator.validate_receipt(receipt)
        self.assertTrue(any("timezone-aware RFC3339" in error for error in errors))

    def test_unexpected_fields_are_rejected(self) -> None:
        receipt = self.load(
            ROOT
            / "fixtures"
            / "human-response-state"
            / "invalid"
            / "unexpected-field.json"
        )
        errors = validator.validate_receipt(receipt)
        self.assertTrue(any("unexpected fields" in error for error in errors))

    def test_glob_arguments_expand_inside_cli(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "one.json").write_text("{}", encoding="utf-8")
            (root / "two.json").write_text("{}", encoding="utf-8")

            paths, errors = validator.expand_path_args(
                [str(root / "*.json")]
            )

            self.assertEqual([], errors)
            self.assertEqual([root / "one.json", root / "two.json"], paths)

    def test_unmatched_glob_returns_clear_error(self) -> None:
        paths, errors = validator.expand_path_args(
            ["fixtures/does-not-exist/*.json"]
        )
        self.assertEqual([], paths)
        self.assertEqual(
            ["no files matched pattern: fixtures/does-not-exist/*.json"],
            errors,
        )

    def test_unconfirmed_response_cannot_grant_execution_authority(self) -> None:
        for authority in ("CONTINUE", "CHOOSE"):
            receipt = {
                "schema_version": "0.1",
                "question_id": "q-negative",
                "response_state": "TIMED_OUT",
                "selected_option": None,
                "decision_source": "SYSTEM",
                "human_interaction_observed": False,
                "human_confirmed": False,
                "agent_authority": authority,
                "observed_at": "2026-07-15T20:00:00Z",
            }
            with self.subTest(authority=authority):
                errors = validator.validate_receipt(receipt)
                self.assertTrue(
                    any("cannot grant CONTINUE or CHOOSE" in error for error in errors)
                )


if __name__ == "__main__":
    unittest.main()
