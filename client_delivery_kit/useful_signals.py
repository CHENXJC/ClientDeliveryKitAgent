"""Useful signal generation for future AgentHub import."""

from __future__ import annotations

from client_delivery_kit.schema import AutomationOpportunity, UsefulSignal


EXECUTION_POLICY = "display_only_text_recommendation_no_execution"


def _usefulness_score(opportunity: AutomationOpportunity) -> int:
    return max(1, min(100, round((opportunity.total_score / 3.8) * 100)))


def generate_useful_signals(opportunities: list[AutomationOpportunity]) -> list[UsefulSignal]:
    signals: list[UsefulSignal] = []
    for opportunity in opportunities:
        signals.append(
            UsefulSignal(
                signal_id=f"signal_{opportunity.opportunity_id}",
                source="client_delivery_kit_agent",
                title=f"{opportunity.priority_level.title()} priority: {opportunity.workflow_area}",
                summary=(
                    f"{opportunity.title} scored {opportunity.total_score} "
                    f"for {opportunity.workflow_area}."
                ),
                category="client_delivery_automation_opportunity",
                usefulness_score=_usefulness_score(opportunity),
                target_agent="agenthub_control_center",
                recommended_action=opportunity.recommended_action,
                status="ready_for_review",
                execution_policy=EXECUTION_POLICY,
            )
        )
    return signals
