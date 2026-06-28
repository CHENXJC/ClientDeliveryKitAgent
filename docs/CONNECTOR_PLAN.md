# Connector Plan

## Current Connector Status

All connectors are planned, optional, or not connected. This project does not connect to any real external system in `CLIENTDELIVERYKIT-001`.

## Planned Connectors

| Connector | Current Status | Purpose | Approval Needed |
| --- | --- | --- | --- |
| local_file | planned | Read synthetic local demo files | No |
| csv_json_demo_data | planned | Load public-safe fixtures | No |
| agenthub_control_center | planned | Metadata and summary integration | No |
| google_docs_planned | not_connected | Future report export | Yes |
| google_sheets_planned | not_connected | Future scorecard export | Yes |
| notion_planned | not_connected | Future workspace summary export | Yes |
| airtable_planned | not_connected | Future structured delivery pipeline | Yes |
| gmail_planned | not_connected | Future draft-only communication plan | Yes, and send remains blocked |
| pdf_export_planned | planned | Future local report export | Yes |

## Connector Readiness Questions

- What data would the connector read?
- Can it write to an external system?
- Could it affect a customer-facing workflow?
- Is rollback possible?
- Is human review required?
- Can the result be shown publicly?

## Blocked Until Future Approval

- automatic customer message sending
- automatic external document updates
- automatic spreadsheet writes to real business systems
- production workspace changes
- external script execution

## Recommended Sequence

1. Build local demo JSON loading.
2. Add report export to local public-safe files.
3. Add AgentHub metadata import.
4. Design connector readiness forms.
5. Only then consider any account-connected workflow.
