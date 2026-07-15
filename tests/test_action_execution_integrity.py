from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "tools" / "validate_action_execution.py"

spec = importlib.util.spec_from_file_location(
    "validate_action_execution", VALIDATOR_PATH
)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class ActionExecutionIntegrityTests(unittest.TestCase):
    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_all_valid_chains_pass(self) -> None:
        fixtures = sorted(
            (ROOT / "fixtures" / "action-execution" / "valid").glob("*.json")
        )
        self.assertGreaterEqual(len(fixtures), 2)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                self.assertEqual(
                    [], validator.validate_chain_document(self.load(fixture))
                )

    def test_all_invalid_chains_fail_closed(self) -> None:
        fixtures = sorted(
            (ROOT / "fixtures" / "action-execution" / "invalid").glob("*.json")
        )
        self.assertGreaterEqual(len(fixtures), 6)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                self.assertTrue(
                    validator.validate_chain_document(self.load(fixture))
                )

    def test_valid_chain_preserves_three_separate_events(self) -> None:
        chain = self.load(
            ROOT
            / "fixtures"
            / "action-execution"
            / "valid"
            / "succeeded-exact-contract.json"
        )
        self.assertEqual("HUMAN", chain["authorization"]["decision_source"])
        self.assertEqual("AGENT", chain["selection"]["decision_source"])
        self.assertEqual("AGENT", chain["execution"]["initiated_by"])
        self.assertEqual("TOOL", chain["execution"]["executed_by"])
        self.assertIsNone(chain["authorization"]["selected_option"])

    def test_action_type_substitution_is_rejected(self) -> None:
        chain = self.load(
            ROOT
            / "fixtures"
            / "action-execution"
            / "invalid"
            / "action-type-mismatch.json"
        )
        errors = validator.validate_chain_document(chain)
        self.assertTrue(any("action_type must match" in error for error in errors))

    def test_action_target_substitution_is_rejected(self) -> None:
        chain = self.load(
            ROOT
            / "fixtures"
            / "action-execution"
            / "invalid"
            / "action-target-mismatch.json"
        )
        errors = validator.validate_chain_document(chain)
        self.assertTrue(any("action_target must match" in error for error in errors))

    def test_action_parameter_substitution_is_rejected(self) -> None:
        chain = self.load(
            ROOT
            / "fixtures"
            / "action-execution"
            / "invalid"
            / "action-parameters-mismatch.json"
        )
        errors = validator.validate_chain_document(chain)
        self.assertTrue(
            any("action_parameters must exactly match" in error for error in errors)
        )

    def test_execution_requires_predeclared_action_contract(self) -> None:
        chain = self.load(
            ROOT
            / "fixtures"
            / "action-execution"
            / "invalid"
            / "missing-action-contract.json"
        )
        errors = validator.validate_chain_document(chain)
        self.assertTrue(any("action_contract is required" in error for error in errors))

    def test_execution_cannot_precede_selection(self) -> None:
        chain = self.load(
            ROOT
            / "fixtures"
            / "action-execution"
            / "invalid"
            / "execution-before-selection.json"
        )
        errors = validator.validate_chain_document(chain)
        self.assertTrue(
            any("cannot precede selection" in error for error in errors)
        )

    def test_success_cannot_hide_execution_error(self) -> None:
        chain = self.load(
            ROOT
            / "fixtures"
            / "action-execution"
            / "invalid"
            / "succeeded-with-error.json"
        )
        errors = validator.validate_chain_document(chain)
        self.assertTrue(
            any("successful execution must have error=null" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
