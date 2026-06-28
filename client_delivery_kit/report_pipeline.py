"""End-to-end public-safe report generation pipeline."""

from __future__ import annotations

from pathlib import Path

from client_delivery_kit.data_loader import load_demo_dataset
from client_delivery_kit.public_summary import build_delivery_summary
from client_delivery_kit.report_builder import build_report, build_report_artifacts
from client_delivery_kit.report_exporter import export_report_bundle
from client_delivery_kit.report_schema import DeliveryReport, ReportArtifacts


def build_demo_report(root: Path | None = None) -> tuple[DeliveryReport, ReportArtifacts]:
    dataset = load_demo_dataset(root=root)
    summary = build_delivery_summary(dataset)
    report = build_report(dataset, summary)
    return report, build_report_artifacts(report)


def generate_demo_report_files(root: Path | None = None) -> dict[str, Path]:
    report, artifacts = build_demo_report(root=root)
    return export_report_bundle(
        markdown=artifacts.markdown,
        json_text=artifacts.json_text,
        csv_text=artifacts.csv_text,
        root=root,
    )
