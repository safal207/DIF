from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "tools" / "validate_agent_selection.py"

spec = importlib.util.spec_from_file_location(
    "validate_agent_selection", VALIDATOR_PATH
)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class AgentSelectionIntegrityTests(unittest.TestCase):
    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_all_valid_pairs_pass(self) -> None:
        fixtures = sorted(
            (ROOT / "fixtures" / "agent-selection" / "valid").glob("*.json")
        )
        self.assertGreaterEqual(len(fixtures), 1)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                self.assertEqual(
                    [], validator.validate_pair_document(self.load(fixture))
                )

    def test_all_invalid_pairs_fail_closed(self) -> None:
        fixtures = sorted(
            (ROOT / "fixtures" / "agent-selection" / "invalid").glob("*.json")
        )
        self.assertGreaterEqual(len(fixtures), 6)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                self.assertTrue(
                    validator.validate_pair_document(self.load(fixture))
                )

    def test_valid_pair_preserves_separate_provenance(self) -> None:
        pair = self.load(
            ROOT
            / "fixtures"
            / "agent-selection"
            / "valid"
            / "explicit-delegation.json"
        )
        self.assertEqual("HUMAN", pair["authorization"]["decision_source"])
        self.assertIsNone(pair["authorization"]["selected_option"])
        self.assertEqual("AGENT", pair["selection"]["decision_source"])
        self.assertEqual("option-b", pair["selection"]["selected_option"])
        self.assertEqual(
            pair["authorization"]["response_id"],
            pair["selection"]["authorization_response_id"],
        )

    def test_timeout_cannot_authorize_agent_choice(self) -> None:
        pair = self.load(
            ROOT
            / "fixtures"
            / "agent-selection"
            / "invalid"
            / "timeout-is-not-delegation.json"
        )
        errors = validator.validate_pair_document(pair)
        self.assertTrue(
            any("must be DELEGATED_TO_AGENT" in error for error in errors)
        )
        self.assertTrue(any("must be CHOOSE" in error for error in errors))

    def test_authorization_link_must_match(self) -> None:
        pair = self.load(
            ROOT
            / "fixtures"
            / "agent-selection"
            / "invalid"
            / "mismatched-authorization-id.json"
        )
        errors = validator.validate_pair_document(pair)
        self.assertTrue(
            any("does not match authorization response_id" in error for error in errors)
        )

    def test_selection_cannot_precede_authorization(self) -> None:
        pair = self.load(
            ROOT
            / "fixtures"
            / "agent-selection"
            / "invalid"
            / "selection-before-authorization.json"
        )
        errors = validator.validate_pair_document(pair)
        self.assertTrue(
            any("cannot precede authorization" in error for error in errors)
        )

    def test_selection_source_must_be_agent(self) -> None:
        pair = self.load(
            ROOT
            / "fixtures"
            / "agent-selection"
            / "invalid"
            / "non-agent-selection-source.json"
        )
        errors = validator.validate_pair_document(pair)
        self.assertTrue(
            any("decision_source must be AGENT" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
