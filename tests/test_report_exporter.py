from pathlib import Path

import pytest

from client_delivery_kit.report_exporter import (
    DEFAULT_CSV_SCORECARD,
    DEFAULT_JSON_REPORT,
    DEFAULT_MARKDOWN_REPORT,
    export_report_bundle,
    public_reports_dir,
    resolve_public_report_path,
    write_public_report,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_resolve_public_report_path_allows_public_reports_only():
    resolved = resolve_public_report_path(DEFAULT_MARKDOWN_REPORT, root=PROJECT_ROOT)

    assert resolved.parent == public_reports_dir(root=PROJECT_ROOT)
    assert resolved.name == DEFAULT_MARKDOWN_REPORT


def test_resolve_public_report_path_rejects_private_output():
    blocked_path = PROJECT_ROOT / "outputs" / "private" / "demo.md"

    with pytest.raises(ValueError, match="outputs/public_reports"):
        resolve_public_report_path(blocked_path, root=PROJECT_ROOT)


def test_resolve_public_report_path_rejects_project_external_path(tmp_path):
    outside = tmp_path / "outside.md"

    with pytest.raises(ValueError, match="outputs/public_reports|project folder"):
        resolve_public_report_path(outside, root=PROJECT_ROOT)


def test_write_public_report_writes_inside_public_reports():
    path = write_public_report("public-safe test", "test_exporter_smoke.md", root=PROJECT_ROOT)

    try:
        assert path.exists()
        assert path.parent == public_reports_dir(root=PROJECT_ROOT)
        assert path.read_text(encoding="utf-8") == "public-safe test"
    finally:
        if path.exists():
            path.unlink()


def test_export_report_bundle_writes_three_default_artifacts():
    paths = export_report_bundle(
        markdown="markdown",
        json_text="{\"ok\": true}",
        csv_text="id\n1\n",
        root=PROJECT_ROOT,
    )

    try:
        assert set(paths) == {"markdown", "json", "csv"}
        assert paths["markdown"].name == DEFAULT_MARKDOWN_REPORT
        assert paths["json"].name == DEFAULT_JSON_REPORT
        assert paths["csv"].name == DEFAULT_CSV_SCORECARD
    finally:
        for path in paths.values():
            if path.exists():
                path.unlink()
