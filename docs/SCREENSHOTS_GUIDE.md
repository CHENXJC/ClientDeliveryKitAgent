# Screenshots Guide

## Purpose

Define public-safe screenshot targets for the future ClientDeliveryKitAgent
showcase.

## Dashboard URL

```text
http://localhost:8535
```

## Recommended Screenshots

| Screenshot | View | Public-Safe Requirement |
| --- | --- | --- |
| `01_dashboard_overview.png` | Overview | Show synthetic demo banner and top metrics |
| `02_client_snapshot.png` | Client Snapshot | Use Demo Local Services Co. only |
| `03_pain_point_diagnosis.png` | Pain Point Diagnosis | Show no real client records |
| `04_opportunity_scorecard.png` | Opportunity Scorecard | Show synthetic scoring only |
| `05_useful_signals.png` | Useful Signals | Show no-execution policy |
| `06_recommended_actions.png` | Recommended Actions | Show template/manual-only actions |
| `07_report_export.png` | Report Export | Show public-safe previews only |
| `08_agenthub_integration.png` | AgentHub Integration | Show local-only AgentHub status |

## Screenshot Directory

```text
docs/images/
```

The directory contains eight captured public-safe PNG screenshots plus
`.gitkeep`.

## Manual Capture Steps

1. Start the dashboard:

```powershell
python -m streamlit run app.py --server.port 8535
```

2. Open:

```text
http://localhost:8535
```

3. Capture each dashboard tab using the filenames above.
4. Save PNG files under `docs/images/`.
5. Stop the Streamlit server after capture.

## Capture Status

Automated screenshot capture completed in CLIENTDELIVERYKIT-008. All eight PNG
files exist, are non-empty, and have valid PNG signatures.

## Captured Screenshot Inventory

| Screenshot | Status |
| --- | --- |
| `docs/images/01_dashboard_overview.png` | Captured |
| `docs/images/02_client_snapshot.png` | Captured |
| `docs/images/03_pain_point_diagnosis.png` | Captured |
| `docs/images/04_opportunity_scorecard.png` | Captured |
| `docs/images/05_useful_signals.png` | Captured |
| `docs/images/06_recommended_actions.png` | Captured |
| `docs/images/07_report_export.png` | Captured |
| `docs/images/08_agenthub_integration.png` | Captured |

## Capture Boundary

- Do not capture `.env`.
- Do not capture terminal output containing local secrets.
- Do not capture private outputs.
- Do not use real customer examples.
- Do not show connector credential forms.

## Status

Screenshot guide complete for
`CLIENTDELIVERYKIT-009-GITHUB-PUBLIC-REPO-FIRST-COMMIT-COMPLETE`.
PNG screenshots are captured and included in the first public commit boundary.
