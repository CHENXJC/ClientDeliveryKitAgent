"""Dashboard data adapters for the Streamlit consultant dashboard."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from client_delivery_kit.data_loader import DemoDataset, load_demo_dataset, project_root
from client_delivery_kit.public_summary import build_delivery_summary
from client_delivery_kit.report_builder import build_report, build_report_artifacts
from client_delivery_kit.report_exporter import (
    DEFAULT_CSV_SCORECARD,
    DEFAULT_JSON_REPORT,
    DEFAULT_MARKDOWN_REPORT,
    public_reports_dir,
)
from client_delivery_kit.report_pipeline import generate_demo_report_files
from client_delivery_kit.report_schema import DeliveryReport, ReportArtifacts
from client_delivery_kit.schema import DeliverySummary


DASHBOARD_URL = "http://localhost:8535"
CURRENT_CHECKPOINT = "CLIENTDELIVERYKIT-008-SCREENSHOT-CAPTURE-AND-SHOWCASE-ASSET-REVIEW-COMPLETE"


@dataclass(frozen=True)
class DashboardData:
    root: Path
    manifest: dict[str, Any]
    dataset: DemoDataset
    summary: DeliverySummary
    report: DeliveryReport
    artifacts: ReportArtifacts
    expected_artifact_paths: dict[str, Path]

    @property
    def top_opportunity(self) -> dict[str, Any]:
        return self.report.opportunities[0]

    @property
    def overview_metrics(self) -> dict[str, Any]:
        return {
            "opportunities": len(self.report.opportunities),
            "useful_signals": len(self.report.useful_signals),
            "recommended_actions": len(self.report.recommended_actions),
            "requires_approval": self.report.delivery_summary.get("requires_approval_count", 0),
        }


def load_manifest(root: Path | None = None) -> dict[str, Any]:
    base = (root or project_root()).resolve()
    with (base / "agent_manifest.json").open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("agent_manifest.json must contain an object.")
    return data


def expected_public_artifact_paths(root: Path | None = None) -> dict[str, Path]:
    public_dir = public_reports_dir(root=root)
    return {
        "markdown": public_dir / DEFAULT_MARKDOWN_REPORT,
        "json": public_dir / DEFAULT_JSON_REPORT,
        "csv": public_dir / DEFAULT_CSV_SCORECARD,
    }


def load_dashboard_data(root: Path | None = None) -> DashboardData:
    base = (root or project_root()).resolve()
    dataset = load_demo_dataset(root=base)
    summary = build_delivery_summary(dataset)
    report = build_report(dataset, summary)
    artifacts = build_report_artifacts(report)
    return DashboardData(
        root=base,
        manifest=load_manifest(root=base),
        dataset=dataset,
        summary=summary,
        report=report,
        artifacts=artifacts,
        expected_artifact_paths=expected_public_artifact_paths(root=base),
    )


def generate_public_demo_artifacts(root: Path | None = None) -> dict[str, Path]:
    return generate_demo_report_files(root=(root or project_root()).resolve())


def pain_point_rows(data: DashboardData) -> list[dict[str, Any]]:
    return [
        {
            "id": item["pain_point_id"],
            "workflow_area": item["workflow_area"],
            "severity": item["severity"],
            "frequency": item["frequency"],
            "bottleneck": item["bottleneck_type"],
            "approval_required": item["approval_required"],
            "impact_summary": item["impact_summary"],
        }
        for item in data.report.pain_points
    ]


def opportunity_rows(data: DashboardData) -> list[dict[str, Any]]:
    return [
        {
            "opportunity_id": item["opportunity_id"],
            "title": item["title"],
            "workflow_area": item["workflow_area"],
            "impact": item["impact_score"],
            "urgency": item["urgency_score"],
            "automation_fit": item["automation_fit_score"],
            "effort": item["implementation_effort_score"],
            "risk": item["risk_score"],
            "total_score": item["total_score"],
            "priority": item["priority_level"],
            "agenthub_target": item["agenthub_target"],
        }
        for item in data.report.opportunities
    ]


def useful_signal_rows(data: DashboardData) -> list[dict[str, Any]]:
    return [
        {
            "signal_id": item["signal_id"],
            "title": item["title"],
            "usefulness_score": item["usefulness_score"],
            "target_agent": item["target_agent"],
            "recommended_action": item["recommended_action"],
            "execution_policy": item["execution_policy"],
            "status": item["status"],
        }
        for item in data.report.useful_signals
    ]


def recommended_action_rows(data: DashboardData) -> list[dict[str, Any]]:
    return [
        {
            "action_id": item["action_id"],
            "label": item["label"],
            "action_type": item["action_type"],
            "execution_mode": item["execution_mode"],
            "risk_level": item["risk_level"],
            "requires_approval": item["requires_approval"],
            "safety_note": item["safety_note"],
            "status": item["status"],
        }
        for item in data.report.recommended_actions
    ]


def connector_rows(data: DashboardData) -> list[dict[str, Any]]:
    return [
        {
            "connector_id": item.get("connector_id"),
            "label": item.get("label"),
            "status": item.get("status"),
            "mode": item.get("mode"),
            "risk_level": item.get("risk_level"),
            "requires_approval": item.get("requires_approval"),
        }
        for item in data.manifest.get("connectors", [])
    ]
