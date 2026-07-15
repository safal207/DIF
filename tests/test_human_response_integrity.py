from __future__ import annotations

import importlib.util
import json
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
        self.assertGreaterEqual(len(fixtures), 6)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                self.assertEqual([], validator.validate_receipt(self.load(fixture)))

    def test_all_invalid_fixtures_fail(self) -> None:
        fixtures = sorted(
            (ROOT / "fixtures" / "human-response-state" / "invalid").glob("*.json")
        )
        self.assertGreaterEqual(len(fixtures), 3)
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
