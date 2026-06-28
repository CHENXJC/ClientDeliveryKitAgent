"""Markdown, JSON, and CSV report builders for public-safe demo exports."""

from __future__ import annotations

import csv
import json
from io import StringIO

from client_delivery_kit.data_loader import DemoDataset
from client_delivery_kit.report_schema import (
    PUBLIC_SAFE_DISCLAIMER,
    REPORT_ID,
    REPORT_SCHEMA_VERSION,
    DeliveryReport,
    ReportArtifacts,
    ClientSnapshot,
    build_validation_snapshot,
    delivery_summary_counts,
)
from client_delivery_kit.schema import DeliverySummary
from client_delivery_kit.useful_signals import EXECUTION_POLICY


CSV_SCORECARD_FIELDS = [
    "opportunity_id",
    "title",
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
]


def build_report(dataset: DemoDataset, summary: DeliverySummary) -> DeliveryReport:
    intake = dataset.client_intake
    context = dataset.business_context
    return DeliveryReport(
        report_id=REPORT_ID,
        schema_version=REPORT_SCHEMA_VERSION,
        execution_policy=EXECUTION_POLICY,
        client_snapshot=ClientSnapshot(
            company_label=intake.company_label,
            industry=intake.industry,
            team_size_band=intake.team_size_band,
            current_stage=intake.current_stage,
            main_goal=intake.main_goal,
        ),
        business_context_summary={
            "business_model": context.business_model,
            "primary_customer_types": list(context.primary_customer_types),
            "workflow_channels": list(context.workflow_channels),
            "current_operating_pattern": context.current_operating_pattern,
            "consulting_angle": context.consulting_angle,
        },
        delivery_summary=delivery_summary_counts(summary),
        pain_points=[item.to_dict() for item in summary.pain_point_diagnoses],
        opportunities=[item.to_dict() for item in summary.automation_opportunities],
        useful_signals=[item.to_dict() for item in summary.useful_signals],
        recommended_actions=[item.to_dict() for item in summary.recommended_actions],
        safety_notes=[
            PUBLIC_SAFE_DISCLAIMER,
            *summary.safety_notes,
        ],
        agenthub_integration_notes=[
            "Markdown report can become a future AgentHub Report Export artifact.",
            "JSON report can become a future AgentHub ingestion artifact.",
            "CSV scorecard can become a future scorecard summary artifact.",
            "No AgentHub runtime or connector is called by this report builder.",
        ],
        suggested_next_steps=[
            "Review the top high-priority opportunity.",
            "Confirm approval requirements before any customer-facing use.",
            "Use the report as a public-safe demo artifact only.",
            "Plan a Streamlit dashboard after report export tests remain stable.",
        ],
        validation_snapshot=build_validation_snapshot(),
    )


def _markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(str(value) for value in row) + " |" for row in rows]
    return "\n".join([header_row, separator, *body])


def build_markdown_report(report: DeliveryReport) -> str:
    data = report.to_dict()
    client = data["client_snapshot"]
    context = data["business_context_summary"]
    summary = data["delivery_summary"]
    pain_rows = [
        [
            item["pain_point_id"],
            item["workflow_area"],
            item["severity"],
            item["frequency"],
            item["bottleneck_type"],
            item["approval_required"],
        ]
        for item in data["pain_points"]
    ]
    opportunity_rows = [
        [
            item["opportunity_id"],
            item["workflow_area"],
            item["impact_score"],
            item["urgency_score"],
            item["automation_fit_score"],
            item["implementation_effort_score"],
            item["risk_score"],
            item["total_score"],
            item["priority_level"],
        ]
        for item in data["opportunities"]
    ]
    signal_rows = [
        [item["signal_id"], item["category"], item["usefulness_score"], item["status"]]
        for item in data["useful_signals"]
    ]
    action_rows = [
        [
            item["action_id"],
            item["label"],
            item["execution_mode"],
            item["risk_level"],
            item["requires_approval"],
        ]
        for item in data["recommended_actions"]
    ]

    return "\n".join(
        [
            "# AI Automation Opportunity Review for Demo Local Services Co.",
            "",
            "## Public-Safe Disclaimer",
            "",
            PUBLIC_SAFE_DISCLAIMER,
            "",
            "## Demo Client Snapshot",
            "",
            f"- Company label: {client['company_label']}",
            f"- Industry: {client['industry']}",
            f"- Team size band: {client['team_size_band']}",
            f"- Current stage: {client['current_stage']}",
            f"- Main goal: {client['main_goal']}",
            "",
            "## Discovery Summary",
            "",
            summary["discovery_summary"],
            "",
            "## Business Context Summary",
            "",
            f"- Business model: {context['business_model']}",
            f"- Workflow channels: {', '.join(context['workflow_channels'])}",
            f"- Operating pattern: {context['current_operating_pattern']}",
            f"- Consulting angle: {context['consulting_angle']}",
            "",
            "## Pain Point Diagnosis",
            "",
            _markdown_table(
                ["ID", "Workflow Area", "Severity", "Frequency", "Bottleneck", "Approval"],
                pain_rows,
            ),
            "",
            "## Workflow Bottleneck Map",
            "",
            "\n".join(
                f"- {item['workflow_area']}: {item['bottleneck_type']} ({item['impact_summary']})"
                for item in data["pain_points"]
            ),
            "",
            "## Automation Opportunity Scorecard",
            "",
            _markdown_table(
                [
                    "ID",
                    "Area",
                    "Impact",
                    "Urgency",
                    "Fit",
                    "Effort",
                    "Risk",
                    "Total",
                    "Priority",
                ],
                opportunity_rows,
            ),
            "",
            "## Useful Signals",
            "",
            _markdown_table(["ID", "Category", "Usefulness", "Status"], signal_rows),
            "",
            "## Recommended Actions",
            "",
            _markdown_table(["ID", "Label", "Mode", "Risk", "Approval"], action_rows),
            "",
            "## Risk And Approval Notes",
            "",
            "\n".join(f"- {note}" for note in data["safety_notes"]),
            "",
            "## AgentHub Integration Notes",
            "",
            "\n".join(f"- {note}" for note in data["agenthub_integration_notes"]),
            "",
            "## Suggested Next Steps",
            "",
            "\n".join(f"- {step}" for step in data["suggested_next_steps"]),
            "",
            "## Validation Snapshot",
            "",
            f"- Source data: {data['validation_snapshot']['source_data']}",
            f"- JSON validation: {data['validation_snapshot']['json_validation']}",
            f"- Scoring policy: {data['validation_snapshot']['scoring_policy']}",
            f"- Export policy: {data['validation_snapshot']['export_policy']}",
            f"- Execution policy: {report.execution_policy}",
            "",
        ]
    )


def build_json_report(report: DeliveryReport) -> str:
    return json.dumps(report.to_dict(), ensure_ascii=False, indent=2, sort_keys=True)


def build_csv_scorecard(report: DeliveryReport) -> str:
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=CSV_SCORECARD_FIELDS, lineterminator="\n")
    writer.writeheader()
    for opportunity in report.opportunities:
        writer.writerow({field: opportunity[field] for field in CSV_SCORECARD_FIELDS})
    return output.getvalue()


def build_report_artifacts(report: DeliveryReport) -> ReportArtifacts:
    return ReportArtifacts(
        markdown=build_markdown_report(report),
        json_text=build_json_report(report),
        csv_text=build_csv_scorecard(report),
    )
