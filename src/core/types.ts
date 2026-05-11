/**
 * Core TypeScript types for DeepIntent Funnel (DIF).
 *
 * These interfaces model the minimal v0.1 journey:
 * raw signal → context → hypotheses → correction → confirmed intent → graph → action.
 *
 * No external dependencies are required.
 */

/** Raw human expression before it becomes clarified intent. */
export interface Signal {
  id: string;
  type:
    | "text"
    | "drawing"
    | "voice_transcript"
    | "emotion"
    | "screenshot"
    | "note"
    | "file"
    | "dialogue"
    | "word_set"
    | "behavioral_pattern"
    | "other";
  content: string;
  metadata?: Record<string, unknown>;
  createdAt: string;
}

/** Situational frame around a raw signal. */
export interface Context {
  domain:
    | "project"
    | "money"
    | "relationship"
    | "creativity"
    | "fear"
    | "choice"
    | "action"
    | "meaning"
    | "work"
    | "family"
    | "future"
    | "other";
  userGoal?: string;
  constraints?: string[];
  timeframe?: string;
  notes?: string;
}

/** A provisional interpretation of a raw signal. */
export interface MeaningHypothesis {
  id: string;
  text: string;
  confidence?: "low" | "medium" | "high" | "unknown";
  evidence?: string[];
  status: "proposed" | "accepted" | "rejected" | "modified" | "superseded";
}

/** Human feedback that modifies, accepts, or rejects an interpretation. */
export interface Correction {
  id: string;
  targetHypothesisId?: string;
  feedback: string;
  effect: "accept" | "reject" | "modify" | "deepen" | "remove" | "reframe" | "unknown";
  createdAt: string;
}

/** A human-confirmed version of intention. It is versioned and can change later. */
export interface ConfirmedIntent {
  id: string;
  version: number;
  statement: string;
  confirmedByHuman: boolean;
  sourceSignalIds?: string[];
  sourceCorrectionIds?: string[];
  createdAt: string;
}

/** Node inside the intent graph. */
export interface IntentGraphNode {
  id: string;
  type:
    | "goal"
    | "constraint"
    | "cause"
    | "conflict"
    | "value"
    | "risk"
    | "option"
    | "action"
    | "note"
    | "other";
  label: string;
  description?: string;
}

/** Edge inside the intent graph. */
export interface IntentGraphEdge {
  from: string;
  to: string;
  type:
    | "supports"
    | "blocks"
    | "causes"
    | "protects"
    | "depends_on"
    | "conflicts_with"
    | "leads_to"
    | "clarifies"
    | "other";
  description?: string;
}

/** A lightweight graph of confirmed intention, constraints, causes, risks, and actions. */
export interface IntentGraph {
  nodes: IntentGraphNode[];
  edges: IntentGraphEdge[];
}

/** A concrete next step generated after intent clarification. */
export interface ActionOutput {
  id: string;
  type:
    | "document"
    | "task"
    | "prompt"
    | "decision"
    | "message"
    | "plan"
    | "architecture"
    | "strategy"
    | "other";
  title: string;
  description: string;
  dependsOnIntentId: string;
  status?: "proposed" | "accepted" | "done" | "discarded";
}

/** A complete versioned journey from raw signal to confirmed intent and action. */
export interface DIFSession {
  id: string;
  signals: Signal[];
  context?: Context;
  hypotheses: MeaningHypothesis[];
  corrections: Correction[];
  confirmedIntents: ConfirmedIntent[];
  intentGraphs: IntentGraph[];
  actions: ActionOutput[];
  status:
    | "started"
    | "signal_received"
    | "context_captured"
    | "hypotheses_proposed"
    | "correction_needed"
    | "intent_confirmed"
    | "intent_graph_created"
    | "action_proposed"
    | "closed";
  createdAt: string;
  updatedAt: string;
}
