# AgentHub Integration Plan

## Purpose

ClientDeliveryKitAgent should become a spoke project that AgentHubControlCenter can discover, display, and explain without executing real actions.

## Manifest Scan

AgentHub should scan `agent_manifest.json` and identify:

- project path
- category
- status
- demo and safe mode
- next recommended action
- actions
- connectors
- public showcase status

## Action Center

The current action list is metadata-only. All actions use one of the AgentHub action types:

- `display_only`
- `local_link`
- `report_view`
- `command_template`
- `codex_prompt`

No action is currently executable by AgentHub.

## Useful Signals

`CLIENTDELIVERYKIT-002` generates local `UsefulSignal` objects from synthetic demo opportunities. These objects are not pushed to AgentHub runtime; they are future import candidates.

Useful signals can include:

- high-impact automation opportunity detected
- customer-facing action requires approval
- connector readiness incomplete
- demo report ready for review
- public showcase readiness progress

Current object fields are documented in `docs/USEFUL_SIGNALS_SCHEMA.md`.

## Action Center Mapping

`CLIENTDELIVERYKIT-002` generates `RecommendedAction` objects that can later map to AgentHub Action Center cards.

Current restrictions:

- action type is text-only manual guidance
- execution mode is template-only
- higher-risk items require approval
- no generated action can run a command, send a message, write to an external system, or connect a real account

## Summary Export

The current `DeliverySummary` object and `CLIENTDELIVERYKIT-003` report artifacts can later feed AgentHub report sections. They include:

- project positioning
- current checkpoint
- top pain points
- top automation opportunities
- safety and approval notes
- report readiness status

## Report Artifact Mapping

`CLIENTDELIVERYKIT-003` creates three local public-safe artifacts:

- Markdown report: future AgentHub Report Export artifact
- JSON report: future AgentHub ingestion artifact
- CSV scorecard: future AgentHub scorecard summary artifact

The project does not call AgentHub runtime, does not use an AgentHub connector, and does not push artifacts anywhere.

## Dashboard Mapping

`CLIENTDELIVERYKIT-004` adds a local dashboard URL:

```text
http://localhost:8535
```

Future AgentHub integration can show this as a local dashboard link. The action must remain manual-only and local-only. AgentHub must not launch it automatically without user intent.

Dashboard surfaces:

- demo client snapshot
- pain point diagnosis
- opportunity scorecard
- useful signals
- recommended actions
- report artifacts
- connector readiness status

No file upload, credential input, OAuth, live connector, or real action execution is available in the dashboard.

## CLIENTDELIVERYKIT-005 Import Result

AgentHubControlCenter now discovers ClientDeliveryKitAgent through the existing
manifest loader.

| Check | Result |
| --- | --- |
| Manifest path | `F:\AIProjects\ClientDeliveryKitAgent\agent_manifest.json` |
| Manifest status | Valid local manifest |
| Role in AgentHub | Client-facing delivery workflow spoke |
| Dashboard URL | `http://localhost:8535` |
| GitHub status | Local-only / not yet published |
| Public-safe status | Synthetic demo-only |

This import is metadata/documentation only. AgentHub does not call the
ClientDeliveryKitAgent runtime, connect external systems, or execute actions.

## Codex Prompt Generator

AgentHub can later generate prompts for:

- continuing the scoring engine stage
- polishing the delivery report template
- creating public showcase docs
- reviewing connector readiness plans

Generated prompts must remain copy-ready text only and must not auto-run.

## Connector Readiness

All future connectors must be evaluated before implementation:

- data access level
- write capability
- customer-facing impact
- approval requirements
- rollback limitations
- public showcase safety

## Approval Gate

Actions that send, write, update external systems, or process real customer data must be marked `requires_approval=true` and remain blocked until a later approved implementation stage.
