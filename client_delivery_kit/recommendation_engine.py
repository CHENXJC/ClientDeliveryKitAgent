"""Recommended action generation as text-only guidance."""

from __future__ import annotations

from client_delivery_kit.schema import AutomationOpportunity, RecommendedAction


ALLOWED_ACTION_TYPES = {"display_only", "manual_instruction"}
ALLOWED_EXECUTION_MODES = {"template_only", "planned"}


def _risk_level(opportunity: AutomationOpportunity) -> str:
    if opportunity.risk_score >= 4.0:
        return "medium"
    return "low"


def _requires_approval(opportunity: AutomationOpportunity) -> bool:
    return opportunity.risk_score >= 4.0


def generate_recommended_actions(opportunities: list[AutomationOpportunity]) -> list[RecommendedAction]:
    actions: list[RecommendedAction] = []
    for opportunity in opportunities:
        approval = _requires_approval(opportunity)
        actions.append(
            RecommendedAction(
                action_id=f"review_{opportunity.opportunity_id}",
                label=f"Review {opportunity.workflow_area.title()} Opportunity",
                description=(
                    f"Text-only consultant recommendation for {opportunity.workflow_area}: "
                    f"{opportunity.recommended_action}"
                ),
                action_type="manual_instruction",
                execution_mode="template_only",
                risk_level=_risk_level(opportunity),
                requires_approval=approval,
                expected_output="Manual review note for the public-safe delivery summary.",
                safety_note=(
                    "Requires human approval before any customer-facing use."
                    if approval
                    else "Display-only recommendation based on synthetic demo data."
                ),
                status="ready_for_review",
            )
        )
    return actions
