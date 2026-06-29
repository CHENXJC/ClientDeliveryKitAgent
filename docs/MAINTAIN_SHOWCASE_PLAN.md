# Maintain Showcase Plan

Checkpoint:
`CLIENTDELIVERYKIT-011-PROFILE-PIN-OR-MAINTAIN-SHOWCASE-DECISION-COMPLETE`

## Maintain-Showcase Decision

Decision: `enter maintain-showcase`

ClientDeliveryKitAgent has reached the intended public showcase state:

- Public GitHub repository is live.
- README and key docs are accessible.
- 8/8 public-safe screenshots are live.
- AgentHubControlCenter lists it as a published spoke.
- Pin decision is documented as `recommend pin`.
- Safety boundaries are explicit.

The project should now pause feature expansion.

## What To Maintain

- README first-screen clarity.
- Screenshot paths and public-safe images.
- `agent_manifest.json` and `agent_contract.json` metadata.
- Public docs that explain safety, portfolio positioning, and manual use.
- Tests and compile health.
- AgentHub backlink and published spoke status.

## What Not To Add Next

Do not add the following unless a separate explicit future stage asks for it:

- Real connector integration.
- Real client data processing.
- Upload feature.
- OAuth.
- Live email, sheet, Notion, Airtable, Telegram, or Google integration.
- Auto-send or auto-write actions.
- Production workflow execution.
- SaaS or commercialization layer.

## When To Resume Development

Resume only if one of these conditions is true:

- There is a real client scenario that justifies a V2 planning stage.
- The user explicitly requests ClientDeliveryKitAgent V2.
- AgentHubControlCenter starts a live connector pilot and this project becomes
  the selected demo spoke.
- A public screenshot or docs refresh is needed to keep the showcase current.
- A bugfix or test maintenance task is needed.

## Future Enhancement Backlog

Keep these as future backlog items, not current work:

- PDF / DOCX export after public-safe content review.
- Client-ready proposal template.
- Read-only demo connector simulation.
- More sample client scenarios using synthetic data only.
- AgentHub report import view.
- Optional real connector plan with approval gates.

## Current Operating Mode

Maintain showcase, manual pin optional, no feature expansion.
