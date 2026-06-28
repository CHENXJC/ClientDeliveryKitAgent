# MVP Scope

## In Scope For The First Working MVP

- Load public-safe synthetic JSON samples. Completed in `CLIENTDELIVERYKIT-002`.
- Normalize client intake, business context, and pain point data. Completed in `CLIENTDELIVERYKIT-002`.
- Score automation opportunities with deterministic rules. Completed in `CLIENTDELIVERYKIT-002`.
- Produce a structured opportunity scorecard object. Completed in `CLIENTDELIVERYKIT-002`.
- Generate useful signal objects for future AgentHub import. Completed in `CLIENTDELIVERYKIT-002`.
- Generate text-only recommended action objects. Completed in `CLIENTDELIVERYKIT-002`.
- Generate a Markdown delivery report draft from demo data. Completed in `CLIENTDELIVERYKIT-003`.
- Generate JSON report artifact from demo data. Completed in `CLIENTDELIVERYKIT-003`.
- Generate CSV opportunity scorecard artifact from demo data. Completed in `CLIENTDELIVERYKIT-003`.
- Provide a local Streamlit dashboard for reviewing the demo workflow. Completed in `CLIENTDELIVERYKIT-004`.
- Export summary metadata that AgentHubControlCenter can display. Summary object completed; UI import planned.
- Keep all actions local, demo-only, and reviewable. Active boundary.

## Out Of Scope For The First Working MVP

- Real client records.
- Real account connections.
- Automatic customer communication.
- Automatic external document updates.
- Full CRM, ticketing, or billing integration.
- Complex multi-agent execution.
- Paid service integration.

## Automation Opportunity Scoring

The planned scoring engine should be understandable and consultant-friendly. Suggested dimensions:

- Business impact
- Repeatability
- Data availability
- Implementation effort
- Operational risk
- Human review need

The first scoring engine should return a transparent score breakdown, not a black-box recommendation.

## Acceptance Criteria For CLIENTDELIVERYKIT-002

- Data schemas validate the three demo JSON inputs.
- Scoring output is deterministic.
- High-risk or customer-facing opportunities include approval notes.
- Tests cover score calculation and safety labels.
- No external connector code is introduced.

Status: complete.

## Acceptance Criteria For CLIENTDELIVERYKIT-003

- Convert `DeliverySummary` into a public-safe report draft.
- Keep generated output inside `outputs/public_reports/` if file output is added.
- Add tests for report section completeness and safety labels.
- Do not connect real accounts or process real client records.

Status: complete.

## Acceptance Criteria For CLIENTDELIVERYKIT-004

- Add a local Streamlit dashboard for viewing demo reports and scorecards.
- Keep the dashboard local-only and synthetic-demo-only.
- Do not add real connectors or customer data ingestion.
- Include visible safety and approval notes.

Status: complete.

## Acceptance Criteria For CLIENTDELIVERYKIT-005

- Prepare AgentHub import documentation and metadata checks.
- Add showcase screenshot guidance for the dashboard.
- Keep generated artifacts public-safe.
- Do not add real connector operations.
