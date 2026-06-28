"""Demo JSON loading utilities for ClientDeliveryKitAgent."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from client_delivery_kit.schema import BusinessContext, ClientIntake, WorkflowPainPoint
from client_delivery_kit.validators import (
    validate_business_context,
    validate_client_intake,
    validate_workflow_pain_points,
)


DEFAULT_SAMPLE_FILES = {
    "client_intake": Path("sample_data/demo_client_intake.json"),
    "business_context": Path("sample_data/demo_business_context.json"),
    "workflow_pain_points": Path("sample_data/demo_workflow_pain_points.json"),
}


@dataclass(frozen=True)
class DemoDataset:
    client_intake: ClientIntake
    business_context: BusinessContext
    workflow_pain_points: list[WorkflowPainPoint]


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _resolve_demo_json_path(path: str | Path, root: Path | None = None) -> Path:
    base = (root or project_root()).resolve()
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = base / candidate
    resolved = candidate.resolve()
    if resolved != base and base not in resolved.parents:
        raise ValueError("Demo input path must stay inside the project folder.")
    parts = {part.lower() for part in resolved.parts}
    if ".env" in parts or "private" in parts:
        raise ValueError("Demo input path is outside the approved public-safe sample area.")
    if resolved.suffix.lower() != ".json":
        raise ValueError("Demo input must be a JSON file.")
    return resolved


def load_json_file(path: str | Path, root: Path | None = None) -> dict[str, Any]:
    resolved = _resolve_demo_json_path(path, root=root)
    with resolved.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("Demo JSON root must be an object.")
    return data


def load_demo_dataset(root: Path | None = None) -> DemoDataset:
    base = root or project_root()
    client_intake_data = load_json_file(DEFAULT_SAMPLE_FILES["client_intake"], root=base)
    business_context_data = load_json_file(DEFAULT_SAMPLE_FILES["business_context"], root=base)
    workflow_pain_points_data = load_json_file(DEFAULT_SAMPLE_FILES["workflow_pain_points"], root=base)
    return DemoDataset(
        client_intake=validate_client_intake(client_intake_data),
        business_context=validate_business_context(business_context_data),
        workflow_pain_points=validate_workflow_pain_points(workflow_pain_points_data),
    )
