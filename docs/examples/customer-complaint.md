# Example: Customer Complaint to Support Action

**Use case:** support, customer success, product operations  
**Goal:** Show how DIF turns an emotional customer complaint into a clarified support action.

---

## Raw Signal

```text
Everything is broken. This is urgent.
```

This signal is important but not yet specific.

DIF should not dismiss it, overreact to it, or pretend to know the exact problem.

---

## Visible Signals

```json
{
  "visibleSignals": [
    "The customer is frustrated.",
    "The customer believes the issue is urgent.",
    "The affected product area is not specified.",
    "The actual broken behavior is not described.",
    "The business impact is unknown.",
    "The severity cannot be confirmed yet."
  ]
}
```

---

## Meaning Hypotheses

```json
{
  "meaningHypotheses": [
    {
      "id": "hypothesis_service_outage",
      "text": "The customer may be experiencing a broad service outage or unavailable feature.",
      "confidence": "low",
      "status": "proposed"
    },
    {
      "id": "hypothesis_critical_workflow_blocked",
      "text": "The customer may be blocked from completing an important workflow.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_recent_regression",
      "text": "The customer may be seeing a recent regression after a release or data change.",
      "confidence": "low",
      "status": "proposed"
    },
    {
      "id": "hypothesis_expectation_gap",
      "text": "The customer may be using urgent language because the product behavior differs from expectation.",
      "confidence": "low",
      "status": "proposed"
    }
  ]
}
```

---

## Clarifying Questions

```text
1. What exactly is broken?
2. Which page, feature, or workflow is affected?
3. When did it start?
4. Is it affecting one user, one account, or many customers?
5. Is there data loss, payment failure, security risk, or complete business blockage?
6. Can the customer share a screenshot, error message, request ID, or timestamp?
7. What result did the customer expect?
```

---

## Human Correction

Example support reply from the customer:

```text
Checkout is failing for all users in our account. The payment button spins forever after clicking Pay. It started about 20 minutes ago.
```

DIF updates the interpretation:

```json
{
  "correction": {
    "effect": "increase_specificity_and_severity",
    "rejectedInterpretations": [
      "general_product_broken",
      "expectation_gap_only"
    ],
    "strengthenedInterpretations": [
      "checkout_failure",
      "account_wide_impact",
      "payment_flow_blocked",
      "time_sensitive_issue"
    ]
  }
}
```

---

## Confirmed Intent

```text
Investigate an account-wide checkout failure where the payment button spins indefinitely after users click Pay.
```

Human confirmation example:

```text
Yes. Treat this as urgent and route it to the payments/on-call team.
```

---

## Action Output: Support Triage

### Severity Hypothesis

```text
High severity, pending confirmation.
```

Reason:

```text
The issue may block payment completion for all users in one customer account.
```

### Routing Suggestion

```text
Payments / checkout owner or on-call engineering.
```

### Immediate Next Action

```text
Collect account ID, timestamp, browser/device, request ID if available, and payment provider logs for the failed checkout attempt.
```

### Support Response Draft

```text
Thanks for reporting this. I understand checkout is currently blocked for your account, with the Pay button spinning indefinitely after click. We are treating this as urgent and routing it to the payments team.

To investigate quickly, please send:
- account ID;
- approximate timestamp of the failed attempt;
- browser/device;
- screenshot or screen recording if available;
- any visible error message or request ID.
```

### Engineering Triage Ticket

```text
Title: Investigate account-wide checkout failure: Pay button spins indefinitely

Problem:
A customer reports that checkout fails for all users in their account. After clicking Pay, the payment button spins forever.

Impact:
Potential account-wide payment blockage.

Known context:
- Started around 20 minutes before report.
- Affected flow: checkout/payment.
- Affected scope: all users in one account, pending verification.

Acceptance criteria:
- Confirm whether issue is account-specific or global.
- Check payment provider logs around reported timestamp.
- Check frontend/network errors for checkout submission.
- Confirm whether payment intent/order creation succeeds.
- Provide mitigation or workaround if available.
```

---

## Decoherence Check

Potential drift:

```text
Original confirmed intent:
Investigate checkout failure with Pay button spinning indefinitely.

Drifted action:
Send generic instructions for clearing browser cache.
```

Radar result:

```json
{
  "risk": "high",
  "reason": "The action underreacts to a possible payment-blocking issue and does not route to the correct owner.",
  "recommendedQuestion": "Should this be escalated to payments/on-call before suggesting generic troubleshooting?"
}
```

---

## Why This Example Matters

```text
emotional complaint -> clarified problem intent -> severity hypothesis -> routing -> next action
```

DIF helps support teams respect urgency without converting emotional language into unsupported assumptions.
