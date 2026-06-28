"""Public-safe summary builder for the demo workflow."""

from __future__ import annotations

from pathlib import Path

from client_delivery_kit.data_loader import DemoDataset, load_demo_dataset
from client_delivery_kit.pain_point_engine import diagnose_pain_points
from client_delivery_kit.recommendation_engine import generate_recommended_actions
from client_delivery_kit.schema import DeliverySummary
from client_delivery_kit.scoring_engine import score_opportunities
from client_delivery_kit.useful_signals import generate_useful_signals


def build_delivery_summary(dataset: DemoDataset) -> DeliverySummary:
    diagnoses = diagnose_pain_points(dataset.workflow_pain_points)
    opportunities = score_opportunities(
        dataset.workflow_pain_points,
        business_context=dataset.business_context,
        diagnoses=diagnoses,
    )
    signals = generate_useful_signals(opportunities)
    recommended_actions = generate_recommended_actions(opportunities)
    high_priority_count = sum(1 for item in opportunities if item.priority_level == "high")
    approval_count = sum(1 for item in recommended_actions if item.requires_approval)

    discovery_summary = (
        f"{dataset.client_intake.company_label} is a synthetic {dataset.client_intake.industry} "
        f"demo case focused on {dataset.client_intake.main_goal}."
    )
    return DeliverySummary(
        company_label=dataset.client_intake.company_label,
        discovery_summary=discovery_summary,
        pain_point_diagnoses=diagnoses,
        automation_opportunities=opportunities,
        useful_signals=signals,
        recommended_actions=recommended_actions,
        safety_notes=[
            "Synthetic demo data only.",
            "No external connector is used.",
            "All recommended actions are text-only and require manual review.",
            "Customer-facing use requires a future approval gate.",
        ],
        agenthub_summary={
            "target_agent": "agenthub_control_center",
            "opportunity_count": len(opportunities),
            "useful_signal_count": len(signals),
            "recommended_action_count": len(recommended_actions),
            "high_priority_count": high_priority_count,
            "requires_approval_count": approval_count,
            "execution_policy": "display_only_text_recommendation_no_execution",
        },
    )


def build_demo_delivery_summary(root: Path | None = None) -> DeliverySummary:
    return build_delivery_summary(load_demo_dataset(root=root))
