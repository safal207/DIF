# Human Response State Model v0.1

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

## Validation

Validate a receipt:

```bash
python3 tools/validate_human_response.py \
  fixtures/human-response-state/valid/timed-out.json
```

Validate all known-good fixtures:

```bash
python3 tools/validate_human_response.py \
  fixtures/human-response-state/valid/*.json
```

Run the regression suite:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

The JSON Schema checks the portable record shape. The reference validator also
checks semantic invariants that JSON Schema alone would make difficult to read
and maintain.

## External validation targets

This model was created from concrete failure modes reported in:

- Anthropic Claude Code issue `#77764`: skipping a question is represented as
  “No preference,” which can be interpreted as delegated choice.
- OpenAI Codex issue `#29702`: an unanswered question may auto-resolve and
  continue without an explicit human decision.

The model is implementation-neutral. Products do not need to adopt DIF naming
to use the states, fixtures, or conformance rules.
