# Streamlit Consultant Dashboard

## Purpose

The Streamlit Consultant Dashboard gives a local, public-safe view of the ClientDeliveryKitAgent demo delivery workflow.

## Local URL

```text
http://localhost:8535
```

## Start Command

From the project root:

```powershell
python -m streamlit run app.py --server.port 8535
```

Or use:

```powershell
scripts\run_dashboard.cmd
```

## Sections

- Overview
- Client Snapshot
- Pain Point Diagnosis
- Opportunity Scorecard
- Useful Signals
- Recommended Actions
- Report Export
- AgentHub Integration

## Report Export UI

The dashboard provides:

- Markdown preview
- JSON preview
- CSV preview
- download buttons for in-memory public-safe content
- safe regenerate button for `outputs/public_reports/`

## Safety Boundary

- Synthetic demo data only.
- No real client data.
- No file uploader.
- No credential input.
- No OAuth.
- No external API call.
- No live connector.
- No real action execution.
- Report files can only be written to `outputs/public_reports/`.

## AgentHub Future Use

AgentHub can later show the dashboard URL, report artifact status, useful signal preview, and connector readiness summary. It should treat dashboard launch as manual-only local navigation.
