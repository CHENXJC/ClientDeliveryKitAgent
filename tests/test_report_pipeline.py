import csv
import json
from io import StringIO
from pathlib import Path

from client_delivery_kit.report_exporter import (
    DEFAULT_CSV_SCORECARD,
    DEFAULT_JSON_REPORT,
    DEFAULT_MARKDOWN_REPORT,
)
from client_delivery_kit.report_pipeline import build_demo_report, generate_demo_report_files
from client_delivery_kit.report_schema import PUBLIC_SAFE_DISCLAIMER


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_build_demo_report_returns_all_three_artifacts():
    report, artifacts = build_demo_report(root=PROJECT_ROOT)

    assert report.client_snapshot.company_label == "Demo Local Services Co."
    assert PUBLIC_SAFE_DISCLAIMER in artifacts.markdown
    assert len(json.loads(artifacts.json_text)["opportunities"]) == 4
    assert len(list(csv.DictReader(StringIO(artifacts.csv_text)))) == 4


def test_generate_demo_report_files_writes_markdown_json_csv():
    paths = generate_demo_report_files(root=PROJECT_ROOT)

    assert paths["markdown"].name == DEFAULT_MARKDOWN_REPORT
    assert paths["json"].name == DEFAULT_JSON_REPORT
    assert paths["csv"].name == DEFAULT_CSV_SCORECARD
    assert all(path.exists() for path in paths.values())
    assert PUBLIC_SAFE_DISCLAIMER in paths["markdown"].read_text(encoding="utf-8")
    assert len(json.loads(paths["json"].read_text(encoding="utf-8"))["opportunities"]) == 4
    assert len(list(csv.DictReader(StringIO(paths["csv"].read_text(encoding="utf-8"))))) == 4
