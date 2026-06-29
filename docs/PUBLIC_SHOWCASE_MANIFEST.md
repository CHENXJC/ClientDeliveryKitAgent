# Public Showcase Manifest

## Project

ClientDeliveryKitAgent

## Current Status

`CLIENTDELIVERYKIT-011-PROFILE-PIN-OR-MAINTAIN-SHOWCASE-DECISION-COMPLETE`

## Public Showcase Readiness

| Area | Status | Notes |
| --- | --- | --- |
| Local dashboard | Complete | Streamlit dashboard on `http://localhost:8535` |
| Demo data | Complete | Synthetic demo data only |
| Report artifacts | Complete | Markdown / JSON / CSV under `outputs/public_reports/` |
| AgentHub import | Complete | Valid local manifest discovered by AgentHubControlCenter |
| README first screen | Complete | Clear AI Automation Consultant Delivery Kit positioning |
| Public release checklist | Complete | `docs/PUBLIC_RELEASE_CHECKLIST.md` |
| GitHub repo prep decision | Complete | `docs/GITHUB_REPO_PREP_DECISION.md` |
| GitHub public repo creation decision | Complete | `ready_for_repo_creation`; see `docs/GITHUB_PUBLIC_REPO_CREATION_DECISION.md` |
| First public commit manifest | Complete | `docs/FIRST_PUBLIC_COMMIT_MANIFEST.md` |
| Public exclusion manifest | Complete | `docs/PUBLIC_EXCLUSION_MANIFEST.md` |
| Release readiness report | Complete | `docs/RELEASE_READINESS_REPORT.md` |
| Showcase asset checklist | Complete | `docs/SHOWCASE_ASSET_CHECKLIST.md` |
| Sample report summary | Complete | Compact summary in docs; full generated reports stay out of README |
| GitHub repository | Created | `https://github.com/CHENXJC/ClientDeliveryKitAgent` |
| Screenshots | Complete | 8/8 public-safe PNG screenshots under `docs/images/` |
| Live showcase verification | Complete | Repo, raw README, key docs, README images, and 8/8 screenshots return HTTP 200 |
| Portfolio placement decision | Complete | `recommend pin`; keep AgentHubControlCenter as the higher-priority hub pin |
| Maintain-showcase decision | Complete | Enter maintain-showcase; no feature expansion by default |

## AgentHub Portfolio Row

| Project | Category | Role in AgentHub | GitHub status | Backlink status | Manifest status | Public-safe status | Next note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ClientDeliveryKitAgent | Client delivery / AI automation consulting | Client-facing delivery workflow spoke | Published: `https://github.com/CHENXJC/ClientDeliveryKitAgent` | Backlink live | Valid published manifest | Public-safe synthetic demo | Recommend pin if slot available / maintain showcase |

## Public-Safe Boundary

- No real client data.
- No credentials.
- No live connector.
- No external API.
- No real action execution.
- GitHub publication is verified as a public-safe live showcase.
- No force push, real connector, real action execution, or private output
  publication in this stage.

## Output Tracking Decision

Generated files under `outputs/public_reports/` are public-safe demo artifacts,
but they remain ignored by default for the future public repository. The public
showcase should include `docs/SAMPLE_DELIVERY_REPORT_SUMMARY.md` and regenerate
full demo reports locally when needed.

## Live Showcase Verification

See `docs/LIVE_SHOWCASE_VERIFICATION.md`.

Summary:

- Repository page, raw README, project status, and key docs return HTTP 200.
- README preview images are 3/3 HTTP 200.
- Dashboard screenshots are 8/8 HTTP 200 as `image/png`.
- Remote tree safety passed with unsafe tracked paths = 0.
- `outputs/public_reports/` tracks only `.gitkeep`.

## Profile Pin And Maintain-Showcase Decision

See:

- `docs/PROFILE_PIN_DECISION.md`
- `docs/GITHUB_PROFILE_PIN_GUIDE.md`
- `docs/PORTFOLIO_POSITIONING.md`
- `docs/MAINTAIN_SHOWCASE_PLAN.md`

Summary:

- Pin decision: `recommend pin`.
- Pinned order: AgentHubControlCenter first, ClientDeliveryKitAgent second if a
  slot is available.
- Maintain decision: enter maintain-showcase and pause feature expansion.
- No profile pin was changed automatically.
