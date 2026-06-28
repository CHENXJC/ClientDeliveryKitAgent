"""Report schema objects for public-safe demo delivery exports."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from client_delivery_kit.schema import DeliverySummary
from client_delivery_kit.useful_signals import EXECUTION_POLICY


REPORT_SCHEMA_VERSION = "clientdeliverykit.report.v1"
REPORT_ID = "clientdeliverykit_demo_delivery_report"
PUBLIC_SAFE_DISCLAIMER = (
    "synthetic demo data only; no real client data; no credentials loaded; "
    "no live connector connected; no external API called; no real action executed"
)


@dataclass(frozen=True)
class ClientSnapshot:
    company_label: str
    industry: str
    team_size_band: str
    current_stage: str
    main_goal: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ValidationSnapshot:
    source_data: str
    json_validation: str
    scoring_policy: str
    export_policy: str
    safety_disclaimer: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DeliveryReport:
    report_id: str
    schema_version: str
    execution_policy: str
    client_snapshot: ClientSnapshot
    business_context_summary: dict[str, Any]
    delivery_summary: dict[str, Any]
    pain_points: list[dict[str, Any]]
    opportunities: list[dict[str, Any]]
    useful_signals: list[dict[str, Any]]
    recommended_actions: list[dict[str, Any]]
    safety_notes: list[str]
    agenthub_integration_notes: list[str]
    suggested_next_steps: list[str]
    validation_snapshot: ValidationSnapshot

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "schema_version": self.schema_version,
            "execution_policy": self.execution_policy,
            "client_snapshot": self.client_snapshot.to_dict(),
            "business_context_summary": dict(self.business_context_summary),
            "delivery_summary": dict(self.delivery_summary),
            "pain_points": list(self.pain_points),
            "opportunities": list(self.opportunities),
            "useful_signals": list(self.useful_signals),
            "recommended_actions": list(self.recommended_actions),
            "safety_notes": list(self.safety_notes),
            "agenthub_integration_notes": list(self.agenthub_integration_notes),
            "suggested_next_steps": list(self.suggested_next_steps),
            "validation_snapshot": self.validation_snapshot.to_dict(),
        }


@dataclass(frozen=True)
class ReportArtifacts:
    markdown: str
    json_text: str
    csv_text: str


def build_validation_snapshot() -> ValidationSnapshot:
    return ValidationSnapshot(
        source_data="sample_data synthetic demo JSON files",
        json_validation="required before release validation",
        scoring_policy="deterministic weighted scoring, no external API",
        export_policy="outputs/public_reports only",
        safety_disclaimer=PUBLIC_SAFE_DISCLAIMER,
    )


def delivery_summary_counts(summary: DeliverySummary) -> dict[str, Any]:
    return {
        "company_label": summary.company_label,
        "discovery_summary": summary.discovery_summary,
        "pain_point_count": len(summary.pain_point_diagnoses),
        "opportunity_count": len(summary.automation_opportunities),
        "useful_signal_count": len(summary.useful_signals),
        "recommended_action_count": len(summary.recommended_actions),
        "requires_approval_count": summary.agenthub_summary.get("requires_approval_count", 0),
        "execution_policy": EXECUTION_POLICY,
    }
