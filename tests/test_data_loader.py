from pathlib import Path

import pytest

from client_delivery_kit.data_loader import load_demo_dataset, load_json_file


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_load_demo_dataset_loads_all_sample_files():
    dataset = load_demo_dataset(root=PROJECT_ROOT)

    assert dataset.client_intake.company_label == "Demo Local Services Co."
    assert dataset.business_context.company_label == "Demo Local Services Co."
    assert len(dataset.workflow_pain_points) == 4


def test_load_json_file_blocks_private_area_before_reading():
    blocked_path = Path("outputs") / "private" / "demo.json"
    with pytest.raises(ValueError, match="approved public-safe"):
        load_json_file(blocked_path, root=PROJECT_ROOT)


def test_load_json_file_blocks_non_json_input():
    with pytest.raises(ValueError, match="JSON"):
        load_json_file("README.md", root=PROJECT_ROOT)
