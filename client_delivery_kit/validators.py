"""Validation helpers for synthetic demo inputs."""

from __future__ import annotations

import re
from typing import Any

from client_delivery_kit.schema import (
    DEMO_NOTICE,
    BusinessContext,
    ClientIntake,
    WorkflowPainPoint,
)

EMAIL_LIKE_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
LONG_NUMBER_RE = re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)")


def _walk_text(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        texts: list[str] = []
        for item in value:
            texts.extend(_walk_text(item))
        return texts
    if isinstance(value, dict):
        texts = []
        for item in value.values():
            texts.extend(_walk_text(item))
        return texts
    return []


def validate_demo_notice(data: dict[str, Any]) -> None:
    if data.get("data_notice") != DEMO_NOTICE:
        raise ValueError("Input must include the approved demo-only data notice.")


def validate_no_contact_details(data: dict[str, Any]) -> None:
    for text in _walk_text(data):
        if EMAIL_LIKE_RE.search(text) or LONG_NUMBER_RE.search(text):
            raise ValueError("Demo input contains contact-like details.")


def validate_client_intake(data: dict[str, Any]) -> ClientIntake:
    validate_demo_notice(data)
    validate_no_contact_details(data)
    intake = ClientIntake.from_dict(data)
    if intake.company_label != "Demo Local Services Co.":
        raise ValueError("Only the approved fictional demo company is supported in this stage.")
    return intake


def validate_business_context(data: dict[str, Any]) -> BusinessContext:
    validate_demo_notice(data)
    validate_no_contact_details(data)
    context = BusinessContext.from_dict(data)
    if context.company_label != "Demo Local Services Co.":
        raise ValueError("Business context must match the demo company label.")
    return context


def validate_workflow_pain_points(data: dict[str, Any]) -> list[WorkflowPainPoint]:
    validate_demo_notice(data)
    validate_no_contact_details(data)
    if data.get("company_label") != "Demo Local Services Co.":
        raise ValueError("Pain point data must match the demo company label.")
    pain_points = []
    seen_ids = set()
    for item in data.get("pain_points", []):
        pain_point = WorkflowPainPoint.from_dict(item)
        if pain_point.pain_point_id in seen_ids:
            raise ValueError(f"Duplicate pain point id: {pain_point.pain_point_id}")
        seen_ids.add(pain_point.pain_point_id)
        pain_points.append(pain_point)
    if not pain_points:
        raise ValueError("At least one demo pain point is required.")
    return pain_points
