# Public-Safe Report Export

## Purpose

The report exporter writes demo report artifacts only to `outputs/public_reports/`.

## Default Artifact Paths

- `outputs/public_reports/clientdeliverykit_demo_report.md`
- `outputs/public_reports/clientdeliverykit_demo_report.json`
- `outputs/public_reports/clientdeliverykit_opportunity_scorecard.csv`

## Export Rules

- Only `.md`, `.json`, and `.csv` are allowed.
- Files must be written directly under `outputs/public_reports/`.
- `outputs/private/` is rejected.
- Project-external paths are rejected.
- `.gitkeep` must not be overwritten.
- The exporter creates `outputs/public_reports/` if needed.

## Required Disclaimer

Every report bundle is generated under this public-safe policy:

```text
synthetic demo data only; no real client data; no credentials loaded; no live connector connected; no external API called; no real action executed
```

## AgentHub Future Use

- Markdown can be shown as a future AgentHub Report Export artifact.
- JSON can be used as a future ingestion artifact.
- CSV can be used as a future scorecard artifact.

No AgentHub runtime call or connector is used in this stage.
