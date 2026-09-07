# ConfirmedIntent admission boundary

`schemas/confirmed-intent.schema.json` describes an already human-confirmed
artifact, not a hypothesis waiting for confirmation. Its `confirmedByHuman`
field is required and must be the boolean `true` (`type: boolean`, `const: true`).
The corresponding TypeScript interface uses the literal type `true`.

A missing flag, `false`, `null`, the number `1`, or the string `"true"` cannot
stand in for confirmation. Unconfirmed input stays in the clarification or
hypothesis flow. Do not migrate old records by rewriting `false` to `true`.

This tightens admission for the existing draft artifact shape. It does not
add a new protocol, replace the Human Response State Model, or change the
meaning of explicit delegation. Delegation and the agent's later selection
remain separate receipts; neither silently becomes confirmation of a
particular intent.

## Checks

Install development-only dependencies with
`python -m pip install -r requirements-schema-tests.txt`, then run:

```sh
python -m unittest discover -s schema_tests -v
npx --yes --package=typescript@5.8.3 tsc --noEmit --strict --target ES2020 schema_tests/confirmed-intent-types.ts
node --test tests/test_demo_rule_matching.mjs
```

The schema tests select Draft 2020-12 from the actual schema, validate the
schema itself and check the expected rejection keyword/path. The timestamp
negative control ensures the installed format checker is active. The
TypeScript negative cases use `@ts-expect-error`, so widening the flag back to
`boolean` fails compilation rather than silently accepting an unconfirmed
artifact. The new CI job also runs the existing Python regressions.

These development dependencies and schema tests are isolated from the
standard-library runtime validators. Missing test dependencies are errors,
not skipped tests or successful conformance results.

## Non-claims

A valid record is an internally consistent assertion of confirmation. A
boolean field is not authentication, a signature, or independent evidence
that a human really consented. Confirmation of intent is also not execution
permission; capability, authority, and action-specific checks remain separate.
This patch does not demonstrate canonical cross-repository integration.
