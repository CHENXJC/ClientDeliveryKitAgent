from pathlib import Path

import pytest

from client_delivery_kit.data_loader import load_json_file
from client_delivery_kit.validators import (
    validate_business_context,
    validate_client_intake,
    validate_demo_notice,
    validate_workflow_pain_points,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_validators_accept_all_demo_sample_files():
    intake = validate_client_intake(load_json_file("sample_data/demo_client_intake.json", root=PROJECT_ROOT))
    context = validate_business_context(load_json_file("sample_data/demo_business_context.json", root=PROJECT_ROOT))
    pain_points = validate_workflow_pain_points(
        load_json_file("sample_data/demo_workflow_pain_points.json", root=PROJECT_ROOT)
    )

    assert intake.company_label == context.company_label
    assert len(pain_points) == 4


def test_demo_notice_is_required():
    with pytest.raises(ValueError, match="demo-only"):
        validate_demo_notice({"data_notice": "not_approved_demo_notice"})


def test_workflow_pain_points_require_unique_ids():
    data = load_json_file("sample_data/demo_workflow_pain_points.json", root=PROJECT_ROOT)
    duplicate = dict(data)
    duplicate["pain_points"] = [dict(data["pain_points"][0]), dict(data["pain_points"][0])]

    with pytest.raises(ValueError, match="Duplicate"):
        validate_workflow_pain_points(duplicate)
