from pathlib import Path

from client_delivery_kit.data_loader import load_demo_dataset
from client_delivery_kit.scoring_engine import score_opportunities
from client_delivery_kit.useful_signals import EXECUTION_POLICY, generate_useful_signals


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_useful_signals_follow_agenthub_ready_shape():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    opportunities = score_opportunities(dataset.workflow_pain_points, dataset.business_context)
    signals = generate_useful_signals(opportunities)

    assert len(signals) == 4
    assert signals[0].execution_policy == EXECUTION_POLICY
    assert signals[0].target_agent == "agenthub_control_center"
    assert 1 <= signals[0].usefulness_score <= 100


def test_useful_signal_required_fields_are_present():
    dataset = load_demo_dataset(root=PROJECT_ROOT)
    opportunities = score_opportunities(dataset.workflow_pain_points, dataset.business_context)
    signal = generate_useful_signals(opportunities)[0].to_dict()

    expected = {
        "signal_id",
        "source",
        "title",
        "summary",
        "category",
        "usefulness_score",
        "target_agent",
        "recommended_action",
        "status",
        "execution_policy",
    }
    assert expected <= set(signal)
