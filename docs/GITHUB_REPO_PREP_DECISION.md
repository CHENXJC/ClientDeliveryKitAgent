# GitHub Repo Prep Decision

Checkpoint:
`CLIENTDELIVERYKIT-009-GITHUB-PUBLIC-REPO-FIRST-COMMIT-COMPLETE`

## Decision

Should create repo: `completed`

ClientDeliveryKitAgent is a strong future public portfolio repo because it
shows client-facing AI automation consulting delivery: intake, pain point
diagnosis, opportunity scoring, useful signals, recommended actions, and
public-safe report export.

The follow-up decision is documented in
`docs/GITHUB_PUBLIC_REPO_CREATION_DECISION.md`.

This stage does not create the repository. The repo should be created only in a
explicit `CLIENTDELIVERYKIT-009` stage after user authorization for git
initialization and publication work.

## Include In Future Public Repo

- Source code under `client_delivery_kit/`
- Streamlit dashboard entrypoint `app.py`
- Synthetic `sample_data/`
- README and project status
- `agent_manifest.json` and `agent_contract.json`
- Public-safe docs
- Tests
- Scripts that only launch local demo views
- `docs/images/` screenshots after capture
- `.gitkeep` files for output directories

## Exclude From Future Public Repo

- `.env`
- credentials, tokens, secrets, private keys, passwords
- `.venv/`, local caches, and Python bytecode
- `outputs/private/`
- full generated report artifacts under `outputs/public_reports/*`
- real client data
- private exports
- local databases

## Generated Report Tracking Decision

Do not commit generated full reports by default.

Rationale:

- They are reproducible from synthetic sample data.
- They can create noisy diffs.
- Keeping only `.gitkeep` plus `docs/SAMPLE_DELIVERY_REPORT_SUMMARY.md` gives a
  cleaner public showcase surface.

If a later stage decides to include one canonical generated artifact, it should
be reviewed as a separate explicit policy change.

## Screenshot Tracking Decision

Commit screenshots after capture.

Recommended screenshot files:

- `docs/images/01_dashboard_overview.png`
- `docs/images/02_client_snapshot.png`
- `docs/images/03_pain_point_diagnosis.png`
- `docs/images/04_opportunity_scorecard.png`
- `docs/images/05_useful_signals.png`
- `docs/images/06_recommended_actions.png`
- `docs/images/07_report_export.png`
- `docs/images/08_agenthub_integration.png`

## Suggested Repo Description

Client-facing AI automation delivery kit for turning synthetic client intake
into pain point diagnosis, automation opportunity scorecards, useful signals,
recommended actions, and public-safe delivery reports.

## Suggested Topics

- `ai-agents`
- `ai-automation`
- `workflow-automation`
- `consulting`
- `client-delivery`
- `streamlit`
- `automation-consultant`
- `useful-signals`
- `public-safe`
- `local-first`
- `agenthub`

## Suggested Future First Commit Message

```text
Publish ClientDeliveryKitAgent public showcase MVP
```

## Risks / Blockers

- Screenshots are not yet captured as PNG assets.
- ClientDeliveryKitAgent is intentionally still a non-git local directory.
- GitHub publication requires an explicit future user request.
- Full generated reports should stay ignored unless a later policy explicitly
  approves tracking a canonical artifact.

## Current Repo Creation Decision

Decision: `public_repo_created_first_commit_complete`

The project has a public GitHub repo target and first public-safe commit.
Dashboard screenshots are captured and included in the public showcase surface.

## Next Action

Proceed to
`CLIENTDELIVERYKIT-010-GITHUB-LIVE-SHOWCASE-VERIFICATION-AND-PORTFOLIO-PLACEMENT-REVIEW`
for live README, screenshot, remote-tree, and portfolio placement review.
