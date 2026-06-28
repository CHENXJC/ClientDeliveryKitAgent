# Delivery Report Builder

## Purpose

The report builder converts the deterministic `DeliverySummary` object into public-safe demo artifacts for consultant delivery review.

## Implemented Modules

- `client_delivery_kit/report_schema.py`
- `client_delivery_kit/report_builder.py`
- `client_delivery_kit/report_exporter.py`
- `client_delivery_kit/report_pipeline.py`

## Markdown Report

The Markdown report includes:

- title
- public-safe disclaimer
- demo client snapshot
- discovery summary
- business context summary
- pain point diagnosis
- workflow bottleneck map
- automation opportunity scorecard
- useful signals
- recommended actions
- risk and approval notes
- AgentHub integration notes
- suggested next steps
- validation snapshot

## JSON Report

The JSON report includes:

- `report_id`
- `schema_version`
- `execution_policy`
- `client_snapshot`
- `delivery_summary`
- `pain_points`
- `opportunities`
- `useful_signals`
- `recommended_actions`
- `safety_notes`
- `validation_snapshot`

## CSV Scorecard

The CSV scorecard includes:

- `opportunity_id`
- `title`
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

## Safety Boundary

Reports are generated from synthetic demo data only. The builder does not call external APIs, connect accounts, execute real actions, or process real customer records.
