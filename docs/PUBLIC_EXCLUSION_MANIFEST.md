# Public Exclusion Manifest

Checkpoint:
`CLIENTDELIVERYKIT-009-GITHUB-PUBLIC-REPO-FIRST-COMMIT-COMPLETE`

## Purpose

Define files and data that must stay out of public GitHub commits.
CLIENTDELIVERYKIT-009 uses this exclusion manifest for the first public-safe
commit.

## Always Exclude

- `.env`
- `.env.*`
- credential files
- token files
- secret files
- password files
- private keys such as `*.pem` and `*.key`
- OAuth files
- `auth/`
- `.venv/`, `venv/`, `env/`
- `__pycache__/`
- `.pytest_cache/`
- `.mypy_cache/`
- `.ruff_cache/`
- `.coverage`
- `htmlcov/`
- `outputs/private/`
- private exports
- real client data
- local databases
- generated private reports
- logs, temp files, and backup files

## Output Exclusion Policy

`outputs/public_reports/` is a public-safe local export target, but generated
full reports remain ignored by default for the future first public commit.

Allowed output boundary files:

- `outputs/.gitkeep`
- `outputs/public_reports/.gitkeep`

Excluded generated artifacts by default:

- `outputs/public_reports/clientdeliverykit_demo_report.md`
- `outputs/public_reports/clientdeliverykit_demo_report.json`
- `outputs/public_reports/clientdeliverykit_opportunity_scorecard.csv`

## Data Exclusion Policy

Only synthetic demo data under `sample_data/` is eligible for public tracking.
Do not add real customer records, account exports, production databases, call
transcripts, meeting notes, invoices, emails, CRM exports, or client files.

## Connector Exclusion Policy

No real connector credentials, OAuth state, Gmail data, Google Sheets data,
Notion data, Airtable data, Telegram data, or GitHub connector state should be
stored in this repository.

## `.gitignore` Coverage

The current `.gitignore` already covers the required default boundaries:

- virtual environments and Python caches
- `.env` files
- key files and `auth/`
- generated output files
- `outputs/private/`
- logs, temp files, and OS metadata

No `.gitignore` change is required for this decision stage.
