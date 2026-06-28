from pathlib import Path

from client_delivery_kit.data_loader import load_json_file
from client_delivery_kit.schema import (
    BusinessContext,
    ClientIntake,
    WorkflowPainPoint,
    workflow_pain_points_from_dict,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_client_intake_schema_parses_demo_file():
    data = load_json_file("sample_data/demo_client_intake.json", root=PROJECT_ROOT)
    intake = ClientIntake.from_dict(data)

    assert intake.company_label == "Demo Local Services Co."
    assert intake.current_tools
    assert intake.to_dict()["main_goal"].startswith("reduce manual admin")


def test_business_context_schema_parses_demo_file():
    data = load_json_file("sample_data/demo_business_context.json", root=PROJECT_ROOT)
    context = BusinessContext.from_dict(data)

    assert context.company_label == "Demo Local Services Co."
    assert "lead intake classification" in context.high_fit
    assert context.to_dict()["workflow_channels"]


def test_workflow_pain_point_schema_parses_all_items():
    data = load_json_file("sample_data/demo_workflow_pain_points.json", root=PROJECT_ROOT)
    pain_points = workflow_pain_points_from_dict(data)

    assert len(pain_points) == 4
    assert all(isinstance(item, WorkflowPainPoint) for item in pain_points)
    assert pain_points[0].pain_point_id == "pp_001"
