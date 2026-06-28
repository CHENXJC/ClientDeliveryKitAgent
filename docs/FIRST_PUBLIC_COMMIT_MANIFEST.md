# First Public Commit Manifest

Checkpoint:
`CLIENTDELIVERYKIT-009-GITHUB-PUBLIC-REPO-FIRST-COMMIT-COMPLETE`

## Purpose

Define the exact public-safe file set for the first GitHub commit. This
manifest is used by the explicit CLIENTDELIVERYKIT-009 stage.

## Include In First Public Commit

### Core Source

- `client_delivery_kit/*.py`

### Dashboard

- `app.py`
- `scripts/run_dashboard.cmd`

### Tests

- `tests/*.py`

### Synthetic Demo Data

- `sample_data/demo_client_intake.json`
- `sample_data/demo_business_context.json`
- `sample_data/demo_workflow_pain_points.json`

### Documentation

- `README.md`
- `PROJECT_STATUS.md`
- `docs/*.md`
- `docs/images/.gitkeep`
- `docs/images/01_dashboard_overview.png`
- `docs/images/02_client_snapshot.png`
- `docs/images/03_pain_point_diagnosis.png`
- `docs/images/04_opportunity_scorecard.png`
- `docs/images/05_useful_signals.png`
- `docs/images/06_recommended_actions.png`
- `docs/images/07_report_export.png`
- `docs/images/08_agenthub_integration.png`

### Project Metadata

- `agent_manifest.json`
- `agent_contract.json`
- `requirements.txt`
- `.gitignore`

### Output Boundaries

- `outputs/.gitkeep`
- `outputs/public_reports/.gitkeep`

## Do Not Include By Default

- Generated full report artifacts under `outputs/public_reports/*`
- Private output files under `outputs/private/`
- Local caches, virtual environments, bytecode, logs, temp files, credentials,
  token files, and secret files
- Any real client data or customer export

## Generated Report Policy

Default decision: commit only `.gitkeep` plus
`docs/SAMPLE_DELIVERY_REPORT_SUMMARY.md`.

The generated Markdown, JSON, and CSV reports are reproducible from synthetic
demo data and can create noisy diffs. If a later stage wants one canonical
generated sample artifact, that should be a separate explicit policy change.

## Screenshot Policy

Commit screenshots after capture and review. The screenshot directory now
contains 8/8 public-safe PNG files.

## Future Exact Stage

This manifest was used during
`CLIENTDELIVERYKIT-009-GITHUB-PUBLIC-REPO-FIRST-COMMIT`. Future changes should
continue to exclude generated full reports, private outputs, caches,
credentials, and real client data unless a later explicit policy changes.
