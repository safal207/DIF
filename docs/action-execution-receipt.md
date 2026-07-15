# Action Execution Receipt v0.1

The Action Execution Receipt records what an agent or tool actually attempted
after a human explicitly delegated a choice and the agent selected an option.

## Core invariant

> An execution is valid only when it references a valid Agent Selection Receipt
> and its action type, target, and parameters exactly match the selected action
> contract.

## Three-event chain

```text
HumanResponseReceipt
  response_state = DELEGATED_TO_AGENT
  decision_source = HUMAN
  agent_authority = CHOOSE
        ↓ authorizes
AgentSelectionReceipt
  decision_source = AGENT
  selected_option = send-follow-up
  action_contract = {
    action_type: send_email,
    action_target: customer-123,
    parameters: { template: follow-up }
  }
        ↓ authorizes
ActionExecutionReceipt
  initiated_by = AGENT
  executed_by = TOOL
  action_type = send_email
  action_target = customer-123
  action_parameters = { template: follow-up }
```

The three records must remain separate. The execution receipt cannot rewrite the
human authorization or the agent selection.

## Receipt

```json
{
  "schema_version": "0.1",
  "execution_id": "ex-789",
  "question_id": "q-123",
  "selection_id": "as-456",
  "selected_option": "send-follow-up",
  "action_type": "send_email",
  "action_target": "customer-123",
  "action_parameters": {
    "template": "follow-up"
  },
  "initiated_by": "AGENT",
  "executed_by": "TOOL",
  "execution_status": "SUCCEEDED",
  "started_at": "2026-07-15T20:00:02Z",
  "completed_at": "2026-07-15T20:00:03Z",
  "error": null
}
```

## Action contract

`AgentSelectionReceipt.action_contract` is optional for selections that do not
lead to an external action. It is required before an Action Execution Receipt
can validate.

The contract has exactly three fields:

```json
{
  "action_type": "send_email",
  "action_target": "customer-123",
  "parameters": {
    "template": "follow-up"
  }
}
```

Execution matching is exact:

- `action_type` must match;
- `action_target` must match;
- `action_parameters` must deep-equal `parameters`.

An agent cannot silently change a recipient, operation, amount, template,
priority, or any other parameter after selection.

## Validation

Validate accepted chains:

```bash
python3 tools/validate_action_execution.py \
  "fixtures/action-execution/valid/*.json"
```

A chain fixture contains all three records:

```json
{
  "authorization": {},
  "selection": {},
  "execution": {}
}
```

The validator checks:

1. the human authorization and agent selection form a valid pair;
2. the selection contains a valid action contract;
3. execution references the exact `selection_id`;
4. question and selected option match;
5. action type, target, and parameters match exactly;
6. execution starts after selection and completes after it starts;
7. session identifiers match when both are present;
8. `initiated_by` is `AGENT`;
9. the executor is attributed as `AGENT`, `TOOL`, or `SYSTEM`;
10. successful executions have `error: null`;
11. failed executions include a non-empty error.

## Failure is still provenance

A failed attempt can be a valid receipt when it exactly matches the authorized
action and truthfully reports `execution_status: FAILED` with an error. The
receipt proves what was attempted; it does not claim the external operation
succeeded.

## Scope limits

This version validates one chain at a time. It does not yet prevent replay or
multiple executions from one selection, enforce global ID uniqueness, or sign
records cryptographically. Those controls belong in a later ledger, DRP, or
idempotency policy layer.
