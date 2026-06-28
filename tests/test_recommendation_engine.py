from pathlib import Path

from client_delivery_kit.data_loader import load_demo_dataset
from client_delivery_kit.public_summary import build_demo_delivery_summary
from client_delivery_kit.recommendation_engine import generate_recommended_actions
from client_delivery_kit.scoring_engine import score_opportunities


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_recommended_actions_are_text_only_templates():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    opportunities = score_opportunities(dataset.workflow_pain_points, dataset.business_context)
    actions = generate_recommended_actions(opportunities)

    assert len(actions) == 4
    assert {action.action_type for action in actions} == {"manual_instruction"}
    assert {action.execution_mode for action in actions} == {"template_only"}
    assert all(action.status == "ready_for_review" for action in actions)


def test_recommended_actions_mark_review_for_higher_risk_items():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    opportunities = score_opportunities(dataset.workflow_pain_points, dataset.business_context)
    actions = generate_recommended_actions(opportunities)

    assert any(action.requires_approval for action in actions)
    assert all(action.risk_level in {"low", "medium"} for action in actions)


def test_public_summary_builds_agenthub_ready_counts():
    summary = build_demo_delivery_summary(root=PROJECT_ROOT)
    data = summary.to_dict()

    assert data["company_label"] == "Demo Local Services Co."
    assert data["agenthub_summary"]["opportunity_count"] == 4
    assert data["agenthub_summary"]["useful_signal_count"] == 4
    assert data["agenthub_summary"]["recommended_action_count"] == 4
    assert data["agenthub_summary"]["requires_approval_count"] >= 1
