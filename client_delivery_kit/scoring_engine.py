"""Deterministic automation opportunity scoring."""

from __future__ import annotations

from client_delivery_kit.pain_point_engine import diagnose_pain_points
from client_delivery_kit.schema import (
    AutomationOpportunity,
    BusinessContext,
    PainPointDiagnosis,
    WorkflowPainPoint,
)


SEVERITY_SCORE = {
    "high": 5.0,
    "medium": 3.5,
    "low": 2.0,
}

FREQUENCY_SCORE = {
    "daily": 5.0,
    "weekly": 3.5,
    "monthly": 2.0,
}


def _score_from_map(value: str, mapping: dict[str, float], default: float = 2.5) -> float:
    return mapping.get(value.lower().strip(), default)


def _fit_score(pain_point: WorkflowPainPoint, business_context: BusinessContext | None) -> float:
    text = f"{pain_point.workflow_area} {pain_point.automation_opportunity}".lower()
    high_markers = ["summarize", "structured", "checklist", "digest", "classification"]
    medium_markers = ["draft", "assignment", "faq"]
    if any(marker in text for marker in high_markers):
        return 5.0
    if any(marker in text for marker in medium_markers):
        return 4.0
    if business_context:
        high_fit = " ".join(business_context.high_fit).lower()
        medium_fit = " ".join(business_context.medium_fit).lower()
        if pain_point.workflow_area.lower() in high_fit:
            return 5.0
        if pain_point.workflow_area.lower() in medium_fit:
            return 4.0
    return 3.0


def _implementation_effort_score(pain_point: WorkflowPainPoint) -> float:
    text = f"{pain_point.workflow_area} {pain_point.automation_opportunity}".lower()
    if any(marker in text for marker in ["summary", "summarize", "checklist", "digest"]):
        return 2.0
    if "draft" in text:
        return 3.0
    return 3.5


def _risk_score(pain_point: WorkflowPainPoint, diagnosis: PainPointDiagnosis) -> float:
    text = f"{pain_point.approval_note} {pain_point.workflow_area} {diagnosis.bottleneck_type}".lower()
    if any(marker in text for marker in ["blocked", "customer", "sending", "quote"]):
        return 4.0
    if "internal" in text:
        return 2.0
    return 3.0


def _priority_level(total_score: float) -> str:
    if total_score >= 3.0:
        return "high"
    if total_score >= 2.4:
        return "medium"
    if total_score >= 1.8:
        return "low"
    return "watchlist"


def _agenthub_target(priority_level: str) -> str:
    if priority_level in {"high", "medium"}:
        return "useful_signals"
    return "report_export"


def _recommended_action(priority_level: str, pain_point: WorkflowPainPoint) -> str:
    if priority_level == "high":
        return f"Prioritize a demo-only pilot for {pain_point.workflow_area} with manual review."
    if priority_level == "medium":
        return f"Add {pain_point.workflow_area} to the consultant review backlog."
    if priority_level == "low":
        return f"Track {pain_point.workflow_area} as a later workflow improvement."
    return f"Keep {pain_point.workflow_area} on watchlist until stronger business impact is shown."


def score_opportunities(
    pain_points: list[WorkflowPainPoint],
    business_context: BusinessContext | None = None,
    diagnoses: list[PainPointDiagnosis] | None = None,
) -> list[AutomationOpportunity]:
    diagnosis_items = diagnoses or diagnose_pain_points(pain_points)
    diagnosis_by_id = {item.pain_point_id: item for item in diagnosis_items}
    opportunities: list[AutomationOpportunity] = []

    for index, pain_point in enumerate(pain_points, start=1):
        diagnosis = diagnosis_by_id[pain_point.pain_point_id]
        impact_score = _score_from_map(pain_point.severity, SEVERITY_SCORE)
        urgency_score = _score_from_map(pain_point.frequency, FREQUENCY_SCORE)
        automation_fit_score = _fit_score(pain_point, business_context)
        implementation_effort_score = _implementation_effort_score(pain_point)
        risk_score = _risk_score(pain_point, diagnosis)
        total_score = round(
            0.30 * impact_score
            + 0.25 * urgency_score
            + 0.25 * automation_fit_score
            - 0.10 * implementation_effort_score
            - 0.10 * risk_score,
            2,
        )
        priority_level = _priority_level(total_score)
        opportunities.append(
            AutomationOpportunity(
                opportunity_id=f"opp_{index:03d}",
                title=pain_point.automation_opportunity.title(),
                related_pain_point_ids=[pain_point.pain_point_id],
                workflow_area=pain_point.workflow_area,
                impact_score=impact_score,
                urgency_score=urgency_score,
                automation_fit_score=automation_fit_score,
                implementation_effort_score=implementation_effort_score,
                risk_score=risk_score,
                total_score=total_score,
                priority_level=priority_level,
                recommended_action=_recommended_action(priority_level, pain_point),
                agenthub_target=_agenthub_target(priority_level),
                explanation=(
                    "Weighted score = 0.30 impact + 0.25 urgency + 0.25 automation fit "
                    "- 0.10 implementation effort - 0.10 risk."
                ),
            )
        )

    return sorted(opportunities, key=lambda item: item.total_score, reverse=True)
