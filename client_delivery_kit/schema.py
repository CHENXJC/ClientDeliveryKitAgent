"""Data schema objects for the demo-only client delivery workflow."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


DEMO_NOTICE = "demo_only_synthetic_data_no_real_customer_information"


def _require_mapping(data: dict[str, Any], key: str) -> dict[str, Any]:
    value = data.get(key)
    if not isinstance(value, dict):
        raise ValueError(f"Expected object field: {key}")
    return value


def _require_list(data: dict[str, Any], key: str) -> list[Any]:
    value = data.get(key)
    if not isinstance(value, list):
        raise ValueError(f"Expected list field: {key}")
    return value


def _require_str(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Expected non-empty text field: {key}")
    return value


def _string_list(data: dict[str, Any], key: str) -> list[str]:
    values = _require_list(data, key)
    if not all(isinstance(value, str) and value.strip() for value in values):
        raise ValueError(f"Expected text list field: {key}")
    return list(values)


@dataclass(frozen=True)
class ClientIntake:
    data_notice: str
    company_label: str
    industry: str
    team_size_band: str
    region_label: str
    contact_role: str
    current_stage: str
    main_goal: str
    current_tools: list[str]
    top_constraints: list[str]
    success_definition: list[str]
    safety_notes: list[str]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ClientIntake":
        profile = _require_mapping(data, "client_profile")
        summary = _require_mapping(data, "intake_summary")
        return cls(
            data_notice=_require_str(data, "data_notice"),
            company_label=_require_str(profile, "company_label"),
            industry=_require_str(profile, "industry"),
            team_size_band=_require_str(profile, "team_size_band"),
            region_label=_require_str(profile, "region_label"),
            contact_role=_require_str(profile, "contact_role"),
            current_stage=_require_str(profile, "current_stage"),
            main_goal=_require_str(summary, "main_goal"),
            current_tools=_string_list(summary, "current_tools"),
            top_constraints=_string_list(summary, "top_constraints"),
            success_definition=_string_list(summary, "success_definition"),
            safety_notes=_string_list(data, "safety_notes"),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class BusinessContext:
    data_notice: str
    company_label: str
    business_model: str
    primary_customer_types: list[str]
    workflow_channels: list[str]
    current_operating_pattern: str
    high_fit: list[str]
    medium_fit: list[str]
    low_fit_or_blocked: list[str]
    consulting_angle: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BusinessContext":
        context = _require_mapping(data, "business_context")
        hypothesis = _require_mapping(data, "automation_fit_hypothesis")
        return cls(
            data_notice=_require_str(data, "data_notice"),
            company_label=_require_str(context, "company_label"),
            business_model=_require_str(context, "business_model"),
            primary_customer_types=_string_list(context, "primary_customer_types"),
            workflow_channels=_string_list(context, "workflow_channels"),
            current_operating_pattern=_require_str(context, "current_operating_pattern"),
            high_fit=_string_list(hypothesis, "high_fit"),
            medium_fit=_string_list(hypothesis, "medium_fit"),
            low_fit_or_blocked=_string_list(hypothesis, "low_fit_or_blocked"),
            consulting_angle=_require_str(data, "consulting_angle"),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class WorkflowPainPoint:
    pain_point_id: str
    title: str
    workflow_area: str
    severity: str
    frequency: str
    business_impact: str
    automation_opportunity: str
    approval_note: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "WorkflowPainPoint":
        return cls(
            pain_point_id=_require_str(data, "pain_point_id"),
            title=_require_str(data, "title"),
            workflow_area=_require_str(data, "workflow_area"),
            severity=_require_str(data, "severity"),
            frequency=_require_str(data, "frequency"),
            business_impact=_require_str(data, "business_impact"),
            automation_opportunity=_require_str(data, "automation_opportunity"),
            approval_note=_require_str(data, "approval_note"),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PainPointDiagnosis:
    diagnosis_id: str
    pain_point_id: str
    title: str
    workflow_area: str
    severity: str
    frequency: str
    bottleneck_type: str
    impact_summary: str
    approval_required: bool
    diagnosis_notes: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AutomationOpportunity:
    opportunity_id: str
    title: str
    related_pain_point_ids: list[str]
    workflow_area: str
    impact_score: float
    urgency_score: float
    automation_fit_score: float
    implementation_effort_score: float
    risk_score: float
    total_score: float
    priority_level: str
    recommended_action: str
    agenthub_target: str
    explanation: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class UsefulSignal:
    signal_id: str
    source: str
    title: str
    summary: str
    category: str
    usefulness_score: int
    target_agent: str
    recommended_action: str
    status: str
    execution_policy: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class RecommendedAction:
    action_id: str
    label: str
    description: str
    action_type: str
    execution_mode: str
    risk_level: str
    requires_approval: bool
    expected_output: str
    safety_note: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DeliverySummary:
    company_label: str
    discovery_summary: str
    pain_point_diagnoses: list[PainPointDiagnosis]
    automation_opportunities: list[AutomationOpportunity]
    useful_signals: list[UsefulSignal]
    recommended_actions: list[RecommendedAction]
    safety_notes: list[str]
    agenthub_summary: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "company_label": self.company_label,
            "discovery_summary": self.discovery_summary,
            "pain_point_diagnoses": [item.to_dict() for item in self.pain_point_diagnoses],
            "automation_opportunities": [item.to_dict() for item in self.automation_opportunities],
            "useful_signals": [item.to_dict() for item in self.useful_signals],
            "recommended_actions": [item.to_dict() for item in self.recommended_actions],
            "safety_notes": list(self.safety_notes),
            "agenthub_summary": dict(self.agenthub_summary),
        }


def workflow_pain_points_from_dict(data: dict[str, Any]) -> list[WorkflowPainPoint]:
    items = _require_list(data, "pain_points")
    return [WorkflowPainPoint.from_dict(item) for item in items]
