# Useful Signals Schema

## Purpose

Useful signals are structured summaries that can later be imported into AgentHubControlCenter. In `CLIENTDELIVERYKIT-002`, they are local Python objects only.

## Required Fields

Each `UsefulSignal` includes:

- `signal_id`
- `source`
- `title`
- `summary`
- `category`
- `usefulness_score`
- `target_agent`
- `recommended_action`
- `status`
- `execution_policy`

## Fixed Execution Policy

```text
display_only_text_recommendation_no_execution
```

This value means the signal is informational only. It must not trigger an action, connector, customer message, file deletion, or external write.

## Status Values Used In This Stage

- `ready_for_review`

## Category Used In This Stage

- `client_delivery_automation_opportunity`

## AgentHub Target

The target agent is:

```text
agenthub_control_center
```

## Safety Notes

- Signals are generated from synthetic demo data.
- Signals are public-safe summary objects.
- Signals do not call AgentHub runtime code.
- Signals do not execute recommended actions.
- Future real connector work must go through connector readiness and approval gates.
