"""Core package for ClientDeliveryKitAgent demo-only scoring workflows."""

from client_delivery_kit.data_loader import DemoDataset, load_demo_dataset
from client_delivery_kit.public_summary import build_demo_delivery_summary
from client_delivery_kit.report_pipeline import build_demo_report, generate_demo_report_files
from client_delivery_kit.schema import (
    AutomationOpportunity,
    BusinessContext,
    ClientIntake,
    DeliverySummary,
    PainPointDiagnosis,
    RecommendedAction,
    UsefulSignal,
    WorkflowPainPoint,
)

__all__ = [
    "AutomationOpportunity",
    "BusinessContext",
    "ClientIntake",
    "DeliverySummary",
    "DemoDataset",
    "PainPointDiagnosis",
    "RecommendedAction",
    "UsefulSignal",
    "WorkflowPainPoint",
    "build_demo_delivery_summary",
    "build_demo_report",
    "generate_demo_report_files",
    "load_demo_dataset",
]
