# Example: Vague Ticket to Testable Task

**Use case:** QA, support, product, and engineering teams  
**Goal:** Show how DIF turns a vague complaint into a clarified, testable task.

---

## Raw Signal

```text
The page is slow and users are unhappy.
```

This is a common type of input in support, QA, product, and engineering workflows.

It contains a real signal, but it is not yet actionable.

---

## Visible Signals

DIF first extracts what is visible without pretending to know the final intent.

```json
{
  "visibleSignals": [
    "A page is perceived as slow.",
    "Users are unhappy.",
    "The affected page is not specified.",
    "The meaning of slow is not quantified.",
    "The user group is not specified.",
    "The timeframe is missing.",
    "There is no reproduction path yet."
  ]
}
```

---

## Initial Meaning Hypotheses

DIF proposes possible interpretations instead of choosing one too early.

```json
{
  "meaningHypotheses": [
    {
      "id": "hypothesis_frontend_performance",
      "text": "The user may be reporting a frontend performance problem on a specific page.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_backend_latency",
      "text": "The slowness may be caused by API latency, database queries, or backend processing.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_realtime_data_issue",
      "text": "The issue may be related to websocket updates, market data, polling, or delayed UI refresh.",
      "confidence": "low",
      "status": "proposed"
    },
    {
      "id": "hypothesis_ux_expectation_gap",
      "text": "Users may describe the page as slow because the flow feels confusing or gives no loading feedback.",
      "confidence": "low",
      "status": "proposed"
    }
  ]
}
```

---

## Clarifying Questions

Before generating a task, DIF should ask for missing context.

```text
1. Which page or flow is slow?
2. When did the issue start?
3. Which users are affected?
4. What does slow mean here: load time, interaction delay, API response, or data refresh?
5. Is the issue reproducible?
6. Do we have browser, device, environment, timestamp, logs, or screenshots?
7. What is the expected behavior?
```

---

## Human Correction

Example human response:

```text
It is not the whole page. The problem happens when users switch between markets. Prices update with delay, and sometimes the UI looks frozen for several seconds.
```

DIF should treat this as a correction, not as a new unrelated prompt.

```json
{
  "correction": {
    "effect": "narrow_scope",
    "rejectedInterpretations": [
      "whole_page_performance",
      "general_dashboard_redesign"
    ],
    "strengthenedInterpretations": [
      "market_switching_performance",
      "realtime_data_update_delay",
      "ui_freeze_during_switch"
    ]
  }
}
```

---

## Confirmed Intent

After correction, DIF can propose a confirmed intent for human approval.

```text
Possible confirmed intent:
Investigate and document the performance issue that occurs when users switch between markets, especially delayed price updates and temporary UI freezing.
```

Human confirmation example:

```text
Yes, this is correct. Make it a testable engineering ticket.
```

---

## Intent Graph

```json
{
  "nodes": [
    {
      "id": "problem_market_switching_slow",
      "type": "problem",
      "label": "Market switching feels slow"
    },
    {
      "id": "symptom_price_delay",
      "type": "symptom",
      "label": "Prices update with delay"
    },
    {
      "id": "symptom_ui_freeze",
      "type": "symptom",
      "label": "UI appears frozen for several seconds"
    },
    {
      "id": "constraint_reproducible_steps",
      "type": "constraint",
      "label": "Reproduction steps are required"
    },
    {
      "id": "action_create_ticket",
      "type": "action",
      "label": "Create a testable engineering ticket"
    }
  ],
  "edges": [
    {
      "from": "symptom_price_delay",
      "to": "problem_market_switching_slow",
      "type": "evidence_for"
    },
    {
      "from": "symptom_ui_freeze",
      "to": "problem_market_switching_slow",
      "type": "evidence_for"
    },
    {
      "from": "constraint_reproducible_steps",
      "to": "action_create_ticket",
      "type": "required_for"
    }
  ]
}
```

---

## Action Output: Testable Ticket

### Title

```text
Investigate delayed price updates and UI freeze when switching markets
```

### Problem Statement

```text
Users report that switching between markets causes delayed price updates and temporary UI freezing for several seconds.
```

### Scope

```text
This ticket focuses only on market switching behavior, not a full dashboard redesign.
```

### Missing Context To Collect

```text
- Affected page or route.
- User role or segment.
- Environment: production, staging, mobile, desktop.
- Browser and device.
- Approximate timestamp.
- Market pairs or instruments involved.
- Network conditions if known.
- Console/network logs if available.
```

### Reproduction Steps

```text
1. Open the affected market page.
2. Select Market A.
3. Wait until price data is visible.
4. Switch to Market B.
5. Observe price update delay and UI responsiveness.
6. Repeat several times with different markets.
```

### Expected Result

```text
After switching markets, the UI remains responsive and price data updates within the accepted performance threshold.
```

### Actual Result

```text
Price updates are delayed and the UI may appear frozen for several seconds.
```

### Acceptance Criteria

```text
- Reproduction steps are documented.
- Expected and actual behavior are clearly separated.
- Performance threshold is defined or requested.
- Logs or metrics are attached if available.
- The likely layer is identified: frontend rendering, API latency, websocket subscription, cache, or data provider.
- The ticket does not expand into a full redesign without separate confirmation.
```

### Suggested First Diagnostic Checks

```text
- Check browser Network tab during market switching.
- Compare API/websocket response timing before and after switching.
- Check whether old subscriptions are cleaned up correctly.
- Check frontend state updates and rendering spikes.
- Compare behavior across browsers and devices.
```

### Next Best Question

```text
Which exact market page, browser/device, and timestamp should we use for the first reproduction attempt?
```

---

## Decoherence Check

DIF should detect if the task starts drifting.

Example drift:

```text
Original confirmed intent:
Investigate delayed price updates during market switching.

Drifted output:
Redesign the whole dashboard to improve user satisfaction.
```

Radar result:

```json
{
  "risk": "high",
  "reason": "The output expands from a specific performance investigation into a broad redesign without confirmation.",
  "recommendedQuestion": "Should we stay focused on market switching performance before discussing dashboard redesign?"
}
```

---

## Why This Example Matters

This example shows the core DIF value:

```text
vague complaint -> clarified intent -> testable task -> safer action
```

DIF does not assume it knows the user's final intent.

It makes uncertainty visible, asks for correction, and only then produces an action-ready output.
