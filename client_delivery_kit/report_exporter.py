"""Safe file export helpers for public demo reports."""

from __future__ import annotations

from pathlib import Path

from client_delivery_kit.data_loader import project_root


PUBLIC_REPORT_DIR = Path("outputs/public_reports")
DEFAULT_MARKDOWN_REPORT = "clientdeliverykit_demo_report.md"
DEFAULT_JSON_REPORT = "clientdeliverykit_demo_report.json"
DEFAULT_CSV_SCORECARD = "clientdeliverykit_opportunity_scorecard.csv"
ALLOWED_SUFFIXES = {".md", ".json", ".csv"}


def public_reports_dir(root: Path | None = None) -> Path:
    return (root or project_root()).resolve() / PUBLIC_REPORT_DIR


def resolve_public_report_path(filename: str | Path, root: Path | None = None) -> Path:
    base = (root or project_root()).resolve()
    allowed_dir = public_reports_dir(root=base).resolve()
    candidate = Path(filename)
    if candidate.is_absolute():
        resolved = candidate.resolve()
    else:
        resolved = (allowed_dir / candidate).resolve()
    if resolved.parent != allowed_dir:
        raise ValueError("Report exports must be written directly under outputs/public_reports.")
    if resolved.suffix.lower() not in ALLOWED_SUFFIXES:
        raise ValueError("Report export suffix must be .md, .json, or .csv.")
    if ".gitkeep" in resolved.name:
        raise ValueError("Report exporter must not overwrite .gitkeep.")
    if "private" in {part.lower() for part in resolved.parts}:
        raise ValueError("Report exports must not target private output paths.")
    if base not in resolved.parents:
        raise ValueError("Report exports must stay inside the project folder.")
    return resolved


def write_public_report(
    content: str,
    filename: str | Path,
    root: Path | None = None,
) -> Path:
    path = resolve_public_report_path(filename, root=root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return path


def export_report_bundle(
    markdown: str,
    json_text: str,
    csv_text: str,
    root: Path | None = None,
) -> dict[str, Path]:
    return {
        "markdown": write_public_report(markdown, DEFAULT_MARKDOWN_REPORT, root=root),
        "json": write_public_report(json_text, DEFAULT_JSON_REPORT, root=root),
        "csv": write_public_report(csv_text, DEFAULT_CSV_SCORECARD, root=root),
    }
