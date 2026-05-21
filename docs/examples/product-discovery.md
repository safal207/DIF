# Example: Product Discovery Clarification

**Use case:** product managers, founders, designers, engineering leads  
**Goal:** Show how DIF clarifies a vague product request before turning it into a feature or roadmap item.

---

## Raw Signal

```text
Users want more control over the dashboard.
```

This sounds like a feature request, but it is still ambiguous.

A team could easily jump to building filters, widgets, permissions, layout customization, or advanced settings without knowing what users actually need.

DIF should clarify the intent before feature design starts.

---

## Visible Signals

DIF extracts what is visible without treating it as final product intent.

```json
{
  "visibleSignals": [
    "Users are asking for more control.",
    "The affected product area is the dashboard.",
    "The word control is ambiguous.",
    "The user segment is not specified.",
    "The underlying pain is not specified.",
    "The desired outcome is not specified.",
    "The team may be at risk of jumping into feature design too early."
  ]
}
```

---

## Missing Context

Before defining a feature, DIF should identify what is missing.

```text
- Which users said this?
- What kind of control do they mean?
- What are they trying to accomplish?
- What can they not do today?
- Is this about layout, data visibility, permissions, filters, alerts, export, automation, or workflow ownership?
- Is this a frequent request or one customer-specific request?
- What business outcome would improve if this were solved?
```

---

## Initial Meaning Hypotheses

DIF proposes multiple interpretations instead of choosing one too early.

```json
{
  "meaningHypotheses": [
    {
      "id": "hypothesis_layout_customization",
      "text": "Users may want to customize dashboard layout, widgets, or saved views.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_data_filtering",
      "text": "Users may want more control over filtering, sorting, or segmenting visible data.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_permissions",
      "text": "Users may want role-based control over what different people can see or change.",
      "confidence": "low",
      "status": "proposed"
    },
    {
      "id": "hypothesis_alerts_and_thresholds",
      "text": "Users may want control over alerts, thresholds, or notification rules.",
      "confidence": "low",
      "status": "proposed"
    },
    {
      "id": "hypothesis_workflow_ownership",
      "text": "Users may want to control workflow state, approvals, or operational handoffs from the dashboard.",
      "confidence": "low",
      "status": "proposed"
    }
  ]
}
```

---

## Clarifying Questions

DIF should ask focused discovery questions.

```text
1. Which user segment asked for more control?
2. What action are they trying to complete when the dashboard feels limiting?
3. What does control mean in their words: layout, filters, permissions, alerts, data export, or workflow state?
4. What happens today when they do not have this control?
5. How often does this happen?
6. What would a successful outcome look like for the user?
7. What should not be changed yet?
```

---

## Human Correction

Example human response:

```text
It is mostly support leads. They do not mean layout customization. They want to filter incidents by customer tier, severity, and owner, then save that view for daily triage.
```

DIF treats this as correction and scope narrowing.

```json
{
  "correction": {
    "effect": "narrow_scope",
    "rejectedInterpretations": [
      "layout_customization",
      "permissions",
      "alerts_and_thresholds"
    ],
    "strengthenedInterpretations": [
      "data_filtering",
      "saved_views",
      "support_triage_workflow"
    ]
  }
}
```

---

## Confirmed Intent

After correction, DIF proposes a confirmed product intent.

```text
Support leads need saved dashboard views that let them filter incidents by customer tier, severity, and owner for daily triage.
```

Human confirmation example:

```text
Yes. Do not make this about full dashboard customization yet. Start with saved triage views.
```

---

## Intent Graph

```json
{
  "nodes": [
    {
      "id": "user_support_leads",
      "type": "value",
      "label": "Support leads"
    },
    {
      "id": "problem_daily_triage",
      "type": "problem",
      "label": "Daily incident triage is hard without saved filtered views"
    },
    {
      "id": "need_saved_views",
      "type": "goal",
      "label": "Save reusable dashboard views"
    },
    {
      "id": "constraint_not_layout_customization",
      "type": "constraint",
      "label": "Do not build full layout customization yet"
    },
    {
      "id": "action_discovery_next_step",
      "type": "action",
      "label": "Validate saved triage views with support leads"
    }
  ],
  "edges": [
    {
      "from": "user_support_leads",
      "to": "problem_daily_triage",
      "type": "clarifies"
    },
    {
      "from": "problem_daily_triage",
      "to": "need_saved_views",
      "type": "supports"
    },
    {
      "from": "constraint_not_layout_customization",
      "to": "need_saved_views",
      "type": "protects"
    },
    {
      "from": "need_saved_views",
      "to": "action_discovery_next_step",
      "type": "leads_to"
    }
  ]
}
```

---

## Action Output: Product Discovery Brief

### Title

```text
Clarify saved triage views for support dashboard
```

### Problem Statement

```text
Support leads need a faster way to triage incidents by customer tier, severity, and owner. The current dashboard does not let them easily save and reuse these filtered views.
```

### Confirmed Product Intent

```text
Explore saved dashboard views for support triage, not full dashboard layout customization.
```

### Target Users

```text
Primary: support leads
Secondary: support managers and incident coordinators
```

### User Need

```text
As a support lead, I want to save incident dashboard views by customer tier, severity, and owner so I can quickly run daily triage without rebuilding filters every time.
```

### Out of Scope for Now

```text
- Full dashboard layout customization.
- Role-based permissions.
- Alerting rules.
- Workflow automation.
- Dashboard redesign.
```

### Discovery Questions

```text
1. Which filters are required for the first saved view?
2. Do users need personal saved views, team shared views, or both?
3. How many saved views does a support lead typically need?
4. Should saved views include sorting and visible columns?
5. What is the failure mode if a saved view becomes outdated?
6. What would make this feature successful after one week of use?
```

### Acceptance Criteria for Discovery

```text
- Interview at least 3 support leads.
- Confirm the top 3 required filters.
- Confirm whether saved views should be personal or shared.
- Identify one daily triage workflow where saved views reduce repeated work.
- Decide whether this is a small feature, larger dashboard capability, or not worth building yet.
```

### Next Best Action

```text
Run a 30-minute discovery session with 3 support leads using a mock saved-view workflow.
```

---

## Decoherence Check

DIF should detect if the product work drifts.

Potential drift:

```text
Confirmed intent:
Explore saved dashboard views for support triage.

Drifted output:
Build a complete drag-and-drop dashboard builder with permissions, widgets, alerts, and automation.
```

Radar result:

```json
{
  "risk": "high",
  "reason": "The output expands a narrowed saved-view discovery task into a broad dashboard platform without confirmation.",
  "recommendedQuestion": "Should we stay focused on saved triage views before considering full dashboard customization?"
}
```

---

## Why This Example Matters

This example shows how DIF helps product teams avoid premature feature building.

```text
vague feature request -> possible meanings -> human correction -> confirmed product intent -> discovery action
```

DIF does not treat a vague user request as a complete product requirement.

It clarifies what users are actually trying to achieve before the team builds.
