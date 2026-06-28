"""Deterministic workflow pain point diagnosis."""

from __future__ import annotations

from client_delivery_kit.schema import PainPointDiagnosis, WorkflowPainPoint


def _bottleneck_type(pain_point: WorkflowPainPoint) -> str:
    text = f"{pain_point.title} {pain_point.workflow_area} {pain_point.business_impact}".lower()
    if "scattered" in text or "handoff" in text:
        return "handoff_and_context_loss"
    if "visibility" in text or "backlog" in text:
        return "operations_visibility_gap"
    if "follow-up" in text or "follow up" in text:
        return "manual_follow_up_gap"
    if "quote" in text or "readiness" in text:
        return "quote_readiness_variance"
    return "manual_process_bottleneck"


def _approval_required(pain_point: WorkflowPainPoint) -> bool:
    text = f"{pain_point.approval_note} {pain_point.workflow_area}".lower()
    return any(marker in text for marker in ["customer", "quote", "sending", "blocked", "review required"])


def diagnose_pain_point(pain_point: WorkflowPainPoint) -> PainPointDiagnosis:
    approval_required = _approval_required(pain_point)
    notes = [
        f"Workflow area: {pain_point.workflow_area}.",
        f"Business impact: {pain_point.business_impact}.",
        "Human review is required before customer-facing use." if approval_required else "Internal demo use can stay display-only.",
    ]
    return PainPointDiagnosis(
        diagnosis_id=f"diag_{pain_point.pain_point_id}",
        pain_point_id=pain_point.pain_point_id,
        title=pain_point.title,
        workflow_area=pain_point.workflow_area,
        severity=pain_point.severity,
        frequency=pain_point.frequency,
        bottleneck_type=_bottleneck_type(pain_point),
        impact_summary=f"{pain_point.severity.title()} severity {pain_point.workflow_area} issue occurring {pain_point.frequency}.",
        approval_required=approval_required,
        diagnosis_notes=notes,
    )


def diagnose_pain_points(pain_points: list[WorkflowPainPoint]) -> list[PainPointDiagnosis]:
    return [diagnose_pain_point(pain_point) for pain_point in pain_points]
