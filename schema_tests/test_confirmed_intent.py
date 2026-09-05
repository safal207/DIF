"""Admission checks against the actual canonical schema, not a copied schema."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import unittest

from jsonschema import FormatChecker, validators

ROOT = Path(__file__).resolve().parents[1]


class ConfirmedIntentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / 'schemas/confirmed-intent.schema.json').read_text())
        validator_class = validators.validator_for(cls.schema)
        validator_class.check_schema(cls.schema)
        cls.validator = validator_class(cls.schema, format_checker=FormatChecker())

    def errors_for(self, value):
        record = copy.deepcopy(self.schema['examples'][0])
        record['confirmedByHuman'] = value
        return list(self.validator.iter_errors(record))

    def test_true_is_accepted(self):
        self.assertEqual(self.errors_for(True), [])

    def test_false_is_rejected_by_confirmation_constraint(self):
        errors = self.errors_for(False)
        self.assertTrue(any(e.validator == 'const' and list(e.path) == ['confirmedByHuman'] for e in errors))

    def test_missing_confirmation_is_rejected(self):
        record = copy.deepcopy(self.schema['examples'][0])
        del record['confirmedByHuman']
        self.assertTrue(any(e.validator == 'required' and 'confirmedByHuman' in e.message for e in self.validator.iter_errors(record)))

    def test_null_is_rejected_as_boolean(self):
        self.assertTrue(any(e.validator == 'type' for e in self.errors_for(None)))

    def test_one_is_not_true(self):
        self.assertTrue(any(e.validator == 'type' for e in self.errors_for(1)))

    def test_string_is_not_true(self):
        self.assertTrue(any(e.validator == 'type' for e in self.errors_for('true')))

    def test_invalid_timestamp_is_actually_checked(self):
        record = copy.deepcopy(self.schema['examples'][0])
        record['createdAt'] = 'not-a-timestamp'
        self.assertTrue(any(e.validator == 'format' and list(e.path) == ['createdAt'] for e in self.validator.iter_errors(record)))

    def test_invalid_version_control(self):
        record = copy.deepcopy(self.schema['examples'][0])
        record['version'] = 0
        self.assertTrue(any(e.validator == 'minimum' for e in self.validator.iter_errors(record)))

    def test_schema_draft(self):
        self.assertEqual(type(self.validator).__name__, 'Draft202012Validator')


if __name__ == '__main__':
    unittest.main()
