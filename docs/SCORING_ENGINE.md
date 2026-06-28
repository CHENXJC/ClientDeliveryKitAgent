# Scoring Engine

## Purpose

The scoring engine ranks synthetic automation opportunities for a public-safe consultant delivery workflow. It is deterministic and uses transparent rules so the output can be explained in a delivery report or AgentHub summary.

## Inputs

- `ClientIntake`
- `BusinessContext`
- `WorkflowPainPoint`
- `PainPointDiagnosis`

All inputs must come from the synthetic demo JSON files in `sample_data/` during the current stage.

## Output Object

Each `AutomationOpportunity` includes:

- `opportunity_id`
- `title`
- `related_pain_point_ids`
- `workflow_area`
- `impact_score`
- `urgency_score`
- `automation_fit_score`
- `implementation_effort_score`
- `risk_score`
- `total_score`
- `priority_level`
- `recommended_action`
- `agenthub_target`
- `explanation`

## Formula

```text
total_score =
0.30 * impact_score
+ 0.25 * urgency_score
+ 0.25 * automation_fit_score
- 0.10 * implementation_effort_score
- 0.10 * risk_score
```

## Priority Levels

- `high`: total score >= 3.0
- `medium`: total score >= 2.4
- `low`: total score >= 1.8
- `watchlist`: total score < 1.8

## Safety Boundary

The scoring engine only returns Python objects. It does not send messages, write external systems, call external APIs, or process real customer records.

## AgentHub Mapping

- High and medium opportunities target future AgentHub Useful Signals.
- Lower priority opportunities target future report export summaries.
- All customer-facing recommendations remain manual review items.
