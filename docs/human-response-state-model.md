# Human Response State Model v0.1

Implementation patch: **v0.1.2**

This model preserves the difference between a human decision and a system event
that merely ended a question.

## Core invariant

> No explicit human answer means no confirmed human decision.

Silence, timeout, dismissal, connection loss, and system cancellation must not
be rewritten as a user-selected answer. An agent may choose only after the user
explicitly delegates that choice.

## States

| State | Meaning | Resulting authority |
|---|---|---|
| `PENDING` | The question is still waiting | `STOP_AND_WAIT` |
| `ANSWERED_BY_USER` | The user explicitly selected an option | `CONTINUE` |
| `DECLINED_OPTIONS` | None of the offered options fit | `ASK_FOLLOWUP` |
| `DEFERRED_BY_USER` | The user will answer later | `STOP_AND_WAIT` |
| `DELEGATED_TO_AGENT` | The user explicitly authorized agent choice | `CHOOSE` |
| `TIMED_OUT` | A timer ended the question | `STOP_AND_WAIT` |
| `DISMISSED` | The user closed or dismissed the question | `STOP_AND_WAIT` |
| `CONNECTION_LOST` | The transport failed before an answer | `STOP_AND_WAIT` |
| `CANCELLED_BY_SYSTEM` | The host cancelled the question | `STOP_AND_WAIT` |

## Receipt

```json
{
  "schema_version": "0.1",
  "response_id": "hr-123",
  "question_id": "q-123",
  "response_state": "TIMED_OUT",
  "selected_option": null,
  "decision_source": "SYSTEM",
  "human_interaction_observed": false,
  "human_confirmed": false,
  "agent_authority": "STOP_AND_WAIT",
  "observed_at": "2026-07-15T20:00:00Z"
}
```

`response_id` is optional for standalone response records. It becomes required
when another record, such as an Agent Selection Receipt, needs to reference the
human response precisely.

`observed_at` accepts timezone-aware RFC3339 values using either `Z` or an
explicit offset, for example `2026-07-15T23:00:00+03:00`. Timestamps without a
timezone are rejected.

## Delegation and later agent selection

`DELEGATED_TO_AGENT` records the human act of granting authority. Therefore its
`decision_source` is `HUMAN` and its `selected_option` remains `null`.

A later option chosen by the agent is a separate event and must not overwrite or
masquerade as the human response receipt:

```text
HumanResponseReceipt
  response_id = hr-123
  response_state = DELEGATED_TO_AGENT
  decision_source = HUMAN
  selected_option = null
        ↓ authorizes
AgentSelectionReceipt
  decision_source = AGENT
  selected_option = option-b
  authorization_response_id = hr-123
```

The companion contract and pair validator are documented in
[`agent-selection-receipt.md`](agent-selection-receipt.md).

The Human Response Receipt schema intentionally excludes `AGENT` from
`decision_source`. Agent provenance belongs in the linked Agent Selection
Receipt.

## Validation

Validate a receipt:

```bash
python3 tools/validate_human_response.py \
  fixtures/human-response-state/valid/timed-out.json
```

Validate all known-good fixtures:

```bash
python3 tools/validate_human_response.py \
  "fixtures/human-response-state/valid/*.json"
```

The CLI expands glob patterns itself, so the quoted form works consistently in
Linux, macOS, and Windows shells. An unmatched pattern produces a clear error.

Run the regression suite:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

The JSON Schema checks the portable record shape. The dependency-free reference
validator mirrors the schema's closed field set and also checks semantic
invariants that JSON Schema alone would make difficult to read and maintain.
Unknown fields are rejected rather than silently accepted.

## External validation targets

This model was created from concrete failure modes reported in:

- Anthropic Claude Code issue `#77764`: skipping a question is represented as
  “No preference,” which can be interpreted as delegated choice.
- OpenAI Codex issue `#29702`: an unanswered question may auto-resolve and
  continue without an explicit human decision.

The model is implementation-neutral. Products do not need to adopt DIF naming
to use the states, fixtures, or conformance rules.
