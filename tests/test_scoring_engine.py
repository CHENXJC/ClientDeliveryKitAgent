from pathlib import Path

from client_delivery_kit.data_loader import load_demo_dataset
from client_delivery_kit.pain_point_engine import diagnose_pain_points
from client_delivery_kit.scoring_engine import score_opportunities


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_pain_point_diagnosis_marks_review_needs():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    diagnoses = diagnose_pain_points(dataset.workflow_pain_points)

    assert len(diagnoses) == 4
    assert diagnoses[0].bottleneck_type == "handoff_and_context_loss"
    assert any(item.approval_required for item in diagnoses)


def test_score_opportunities_is_deterministic_and_prioritized():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    opportunities = score_opportunities(
        dataset.workflow_pain_points,
        business_context=dataset.business_context,
    )

    assert len(opportunities) == 4
    assert opportunities[0].opportunity_id == "opp_001"
    assert opportunities[0].total_score == 3.4
    assert opportunities[0].priority_level == "high"
    assert opportunities[-1].total_score <= opportunities[0].total_score


def test_score_formula_fields_are_present():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    opportunity = score_opportunities(dataset.workflow_pain_points, dataset.business_context)[0]
    data = opportunity.to_dict()

    expected = {
        "opportunity_id",
        "title",
        "related_pain_point_ids",
        "workflow_area",
        "impact_score",
        "urgency_score",
        "automation_fit_score",
        "implementation_effort_score",
        "risk_score",
        "total_score",
        "priority_level",
        "recommended_action",
        "agenthub_target",
        "explanation",
    }
    assert expected <= set(data)
