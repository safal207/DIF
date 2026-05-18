/**
 * Q-State Layer TypeScript types for DeepIntent Funnel (DIF).
 *
 * These interfaces model intention as an uncertain evolving state.
 * They are quantum-inspired, but they do not implement quantum computing.
 *
 * No external dependencies are required.
 */

import type {
  ActionOutput,
  ConfirmedIntent,
  Context,
  Correction,
  MeaningHypothesis,
  Signal,
} from "../core/types";

/** Numeric score normalized from 0 to 1. */
export type NormalizedScore = number;

/** A possible meaning represented inside the current intent state. */
export interface PossibleIntent {
  id: string;
  label: string;
  description?: string;
  confidence: NormalizedScore;
  evidence?: string[];
  relatedHypothesisIds?: string[];
}

/**
 * Current map of possible meanings behind one or more raw signals.
 *
 * Product meaning:
 * IntentStateMatrix = current distribution of possible meanings.
 */
export interface IntentStateMatrix {
  id: string;
  sourceSignalIds: string[];
  possibleIntents: PossibleIntent[];
  uncertainty: NormalizedScore;
  createdAt: string;
  updatedAt?: string;
}

/** A focused lens on the full intention state. */
export interface PartialTraceView {
  id: string;
  sourceStateId: string;
  view:
    | "business"
    | "technical"
    | "emotional"
    | "action"
    | "risk"
    | "product"
    | "support"
    | "qa_testability"
    | "other";
  summary: string;
  includedIntentIds?: string[];
  excludedContext?: string[];
  confidence?: NormalizedScore;
}

/** Event that changes the intent state. */
export interface IntentChannel {
  id: string;
  type:
    | "new_signal"
    | "context_added"
    | "clarification_question"
    | "human_correction"
    | "hypothesis_accepted"
    | "hypothesis_rejected"
    | "intent_confirmed"
    | "action_generated"
    | "other";
  fromStateId?: string;
  toStateId: string;
  signal?: Signal;
  context?: Context;
  hypothesis?: MeaningHypothesis;
  correction?: Correction;
  confirmedIntent?: ConfirmedIntent;
  action?: ActionOutput;
  description?: string;
  createdAt: string;
}

/** Drift and alignment result for the current output. */
export interface DecoherenceRadarResult {
  id: string;
  originalSignalIds: string[];
  confirmedIntentId?: string;
  actionOutputId?: string;
  signalAlignment: NormalizedScore;
  intentAlignment: NormalizedScore;
  topicDrift: NormalizedScore;
  assumptionLoad: NormalizedScore;
  actionabilityIntegrity: NormalizedScore;
  overallDecoherenceRisk: NormalizedScore;
  risk: "low" | "medium" | "high";
  reason: string;
  recommendedQuestion?: string;
  createdAt: string;
}

/** Measures whether clarification improved understanding and action readiness. */
export interface ClarityGain {
  id: string;
  before: {
    clarity: NormalizedScore;
    actionability: NormalizedScore;
  };
  after: {
    clarity: NormalizedScore;
    actionability: NormalizedScore;
  };
  clarityGain: NormalizedScore;
  actionabilityGain: NormalizedScore;
  reason?: string;
}

/** Estimates whether the confirmed intent is ready to become action. */
export interface ActionabilityScore {
  id: string;
  confirmedIntentId: string;
  score: NormalizedScore;
  checks: {
    goalClear: boolean;
    domainClear: boolean;
    constraintsKnown: boolean;
    nextActionKnown: boolean;
    risksVisible: boolean;
    humanConfirmed: boolean;
  };
  recommendation:
    | "ask_clarifying_question"
    | "collect_context"
    | "generate_action"
    | "pause_for_human_confirmation";
  reason?: string;
}

/** Optional container for Q-State data inside a DIF session. */
export interface QStateSessionLayer {
  stateMatrices: IntentStateMatrix[];
  partialTraceViews: PartialTraceView[];
  channels: IntentChannel[];
  decoherenceResults: DecoherenceRadarResult[];
  clarityGains: ClarityGain[];
  actionabilityScores: ActionabilityScore[];
}
