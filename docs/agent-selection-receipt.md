# Agent Selection Receipt v0.1

The Agent Selection Receipt records a choice made by an agent after a human has
explicitly delegated that choice.

## Core invariant

> An agent selection is valid only when it references a valid, earlier Human
> Response Receipt with `response_state: DELEGATED_TO_AGENT` and
> `agent_authority: CHOOSE`.

The human authorization and the agent selection are separate events with
separate provenance.

```text
HumanResponseReceipt
  response_id = hr-123
  question_id = q-123
  response_state = DELEGATED_TO_AGENT
  decision_source = HUMAN
  human_confirmed = true
  agent_authority = CHOOSE
  selected_option = null
        ↓ authorizes
AgentSelectionReceipt
  selection_id = as-456
  question_id = q-123
  selected_option = option-b
  decision_source = AGENT
  authorization_response_id = hr-123
```

## Receipt

```json
{
  "schema_version": "0.1",
  "selection_id": "as-456",
  "question_id": "q-123",
  "selected_option": "option-b",
  "decision_source": "AGENT",
  "authorization_response_id": "hr-123",
  "selected_at": "2026-07-15T20:00:01Z",
  "session_id": "session-1",
  "rationale": "Option B best satisfies the stated constraints."
}
```

## Pair validation

The reference validator accepts fixture documents containing both receipts:

```json
{
  "authorization": { "response_id": "hr-123" },
  "selection": { "authorization_response_id": "hr-123" }
}
```

Run it with:

```bash
python3 tools/validate_agent_selection.py \
  "fixtures/agent-selection/valid/*.json"
```

The validator checks:

1. both receipts are independently well formed;
2. the human receipt has a stable `response_id`;
3. the selection references that exact response;
4. both receipts refer to the same question;
5. the authorization is explicit human delegation;
6. the authorization grants `CHOOSE` authority;
7. the selection occurs at or after authorization;
8. session identifiers match when both are present;
9. the human receipt keeps `selected_option: null`;
10. the selection records `decision_source: AGENT`.

## Fail-closed cases

The following do not authorize an agent choice:

- timeout;
- dismissal;
- skipped or declined options;
- connection loss;
- system cancellation;
- a normal option selected by the human;
- an unconfirmed response;
- a receipt granting anything other than `CHOOSE`.

A structurally valid Agent Selection Receipt is not sufficient by itself. The
linked authorization pair must also validate.

## Scope limits

This version validates one pair at a time. It does not yet enforce global
uniqueness of `selection_id`, prevent reuse of one authorization across several
choices, or provide cryptographic signatures. Those controls belong in a later
ledger or DRP integration layer.
