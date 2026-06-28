# Public-Safe Demo Data Plan

## Purpose

The project uses synthetic demo data so that development, screenshots, tests, and future public documentation can be created without exposing real client information.

## Demo Company

The current fictional company label is:

`Demo Local Services Co.`

This label is not intended to identify a real business.

## Allowed Demo Data

- fictional company label
- fictional role labels
- industry category
- workflow descriptions
- generic tool names
- synthetic pain points
- synthetic scoring examples
- public-safe recommendation templates

## Disallowed Data

- real customer records
- real personal contact details
- real account exports
- private business documents
- private output reports
- local database extracts
- production workflow files

## Sample Files

- `sample_data/demo_client_intake.json`
- `sample_data/demo_business_context.json`
- `sample_data/demo_workflow_pain_points.json`

## Future Data Review

Before any new demo file is added, verify:

- it is synthetic
- it contains no real person or customer contact details
- it includes a demo-only notice
- it is safe for public screenshots and README examples
