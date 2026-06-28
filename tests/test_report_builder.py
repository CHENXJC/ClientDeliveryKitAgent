import csv
import json
from io import StringIO
from pathlib import Path

from client_delivery_kit.data_loader import load_demo_dataset
from client_delivery_kit.public_summary import build_delivery_summary
from client_delivery_kit.report_builder import (
    CSV_SCORECARD_FIELDS,
    build_csv_scorecard,
    build_json_report,
    build_markdown_report,
    build_report,
)
from client_delivery_kit.report_schema import PUBLIC_SAFE_DISCLAIMER


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _demo_report():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    summary = build_delivery_summary(dataset)
    return build_report(dataset, summary)


def test_markdown_report_contains_required_sections_and_disclaimer():
    markdown = build_markdown_report(_demo_report())

    assert "## Public-Safe Disclaimer" in markdown
    assert PUBLIC_SAFE_DISCLAIMER in markdown
    assert "## Demo Client Snapshot" in markdown
    assert "## Automation Opportunity Scorecard" in markdown
    assert "## AgentHub Integration Notes" in markdown
    assert "## Validation Snapshot" in markdown


def test_json_report_contains_required_structured_fields():
    data = json.loads(build_json_report(_demo_report()))

    expected = {
        "report_id",
        "schema_version",
        "execution_policy",
        "client_snapshot",
        "delivery_summary",
        "pain_points",
        "opportunities",
        "useful_signals",
        "recommended_actions",
        "safety_notes",
        "validation_snapshot",
    }
    assert expected <= set(data)
    assert data["client_snapshot"]["company_label"] == "Demo Local Services Co."
    assert len(data["opportunities"]) == 4


def test_csv_scorecard_contains_four_opportunities_and_required_headers():
    csv_text = build_csv_scorecard(_demo_report())
    rows = list(csv.DictReader(StringIO(csv_text)))

    assert len(rows) == 4
    assert set(CSV_SCORECARD_FIELDS) == set(rows[0])
    assert rows[0]["opportunity_id"] == "opp_001"
