# Decoherence Radar

**Status:** early concept  
**Parent concept:** DIF Q-State Layer

Decoherence Radar is a DIF module for detecting meaning drift.

In simple terms:

```text
Decoherence Radar = meaning drift detector
```

It helps answer one practical question:

> Are we still acting on the human-confirmed intent, or did the conversation drift into a different task?

---

## Why This Matters

Many workflow failures start before execution:

```text
vague request -> hidden assumption -> confident output -> rework
```

For teams, this can appear as:

- unclear product tickets;
- weak acceptance criteria;
- support requests routed to the wrong place;
- AI agents executing a different task than intended;
- meetings that end with action items disconnected from the original problem.

Decoherence Radar gives DIF a way to monitor this drift before action happens.

---

## Core Inputs

A basic radar compares:

1. the original `Signal`;
2. the current `ConfirmedIntent`;
3. the latest `ActionOutput`;
4. the correction history;
5. the active constraints.

Example:

```text
Original signal:
The page is slow when switching markets.

Confirmed intent:
Investigate websocket subscription behavior during market switching.

Current output:
Redesign the whole dashboard.

Radar finding:
High drift risk. The current output is broader than the confirmed intent.
```

---

## Suggested Metrics

### Signal Alignment

Measures how strongly the current output is connected to the original signal.

```text
0.0 = no visible connection
1.0 = strongly aligned
```

### Intent Alignment

Measures how strongly the current output matches the latest human-confirmed intent.

```text
0.0 = ignores confirmed intent
1.0 = directly supports confirmed intent
```

### Topic Drift

Measures how far the conversation has moved away from the original domain.

```text
0.0 = no drift
1.0 = severe drift
```

### Assumption Load

Measures how many new assumptions were introduced without confirmation.

```text
0.0 = no unconfirmed assumptions
1.0 = many important unconfirmed assumptions
```

### Actionability Integrity

Measures whether the proposed action still follows from the confirmed intent and constraints.

```text
0.0 = action is not justified
1.0 = action is well supported
```

---

## Example Output

```json
{
  "signalAlignment": 0.81,
  "intentAlignment": 0.74,
  "topicDrift": 0.22,
  "assumptionLoad": 0.31,
  "actionabilityIntegrity": 0.68,
  "overallDecoherenceRisk": 0.34,
  "recommendation": "Ask one clarification question before generating the final task."
}
```

---

## Risk Levels

### Low Risk

```text
0.00 - 0.30
```

Recommended behavior:

```text
Proceed with action.
```

### Medium Risk

```text
0.31 - 0.65
```

Recommended behavior:

```text
Ask a clarification question or show the assumption explicitly.
```

### High Risk

```text
0.66 - 1.00
```

Recommended behavior:

```text
Pause execution and ask the human to confirm, correct, or reject the interpretation.
```

---

## Minimal v0.1 Algorithm

Inputs:

- `originalSignalText`;
- `confirmedIntentText`;
- `currentOutputText`;
- `constraints`;
- `corrections`.

Steps:

1. Extract key terms from the original signal.
2. Extract key terms from the confirmed intent.
3. Extract key terms from the current output.
4. Compare overlap and semantic similarity.
5. Detect new unconfirmed assumptions.
6. Detect missing constraints.
7. Produce a risk score and recommendation.

Output:

```json
{
  "risk": "medium",
  "reason": "The output introduces a broader redesign without confirming whether performance debugging was completed.",
  "recommendedQuestion": "Should we stay focused on websocket switching performance before discussing redesign?"
}
```

---

## Design Principle

Decoherence Radar should be strict about drift but humble about interpretation.

It should not say:

```text
You no longer mean this.
```

It should say:

```text
This may be drifting from the confirmed intent. Please confirm or correct.
```

---

## Summary

Decoherence Radar is the first highly visible Q-State module for DIF.

It makes the product value concrete:

```text
Detect meaning drift before AI or teams do the wrong work.
```
