"""Streamlit view helpers for the consultant dashboard.

The functions accept a Streamlit-like module object so tests can validate view
contracts without importing Streamlit.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from client_delivery_kit.dashboard_data import (
    CURRENT_CHECKPOINT,
    DASHBOARD_URL,
    DashboardData,
    connector_rows,
    generate_public_demo_artifacts,
    opportunity_rows,
    pain_point_rows,
    recommended_action_rows,
    useful_signal_rows,
)
from client_delivery_kit.report_schema import PUBLIC_SAFE_DISCLAIMER


SECTION_TITLES = [
    "Overview",
    "Client Snapshot",
    "Pain Point Diagnosis",
    "Opportunity Scorecard",
    "Useful Signals",
    "Recommended Actions",
    "Report Export",
    "AgentHub Integration",
]


def _dataframe(st: Any, rows: list[dict[str, Any]], *, height: int | None = None) -> None:
    if hasattr(st, "dataframe"):
        kwargs: dict[str, Any] = {"width": "stretch", "hide_index": True}
        if height is not None:
            kwargs["height"] = height
        st.dataframe(rows, **kwargs)
    else:
        st.write(rows)


def render_overview(st: Any, data: DashboardData) -> None:
    st.header("Overview")
    st.markdown("AI Automation Consultant delivery kit for synthetic demo workflow review.")
    st.info(PUBLIC_SAFE_DISCLAIMER)
    metrics = data.overview_metrics
    columns = st.columns(4)
    columns[0].metric("Opportunities", metrics["opportunities"])
    columns[1].metric("Useful Signals", metrics["useful_signals"])
    columns[2].metric("Recommended Actions", metrics["recommended_actions"])
    columns[3].metric("Requires Approval", metrics["requires_approval"])
    top = data.top_opportunity
    st.markdown(f"**Project stage:** `{CURRENT_CHECKPOINT}`")
    st.markdown(f"**Synthetic client:** {data.report.client_snapshot.company_label}")
    st.markdown(
        f"**Top opportunity:** {top['title']} "
        f"({top['priority_level']}, score {top['total_score']})"
    )
    st.caption("Local-only, demo-only, no connector, no external API, no real action execution.")


def render_client_snapshot(st: Any, data: DashboardData) -> None:
    st.header("Client Snapshot")
    client = data.report.client_snapshot.to_dict()
    context = data.report.business_context_summary
    st.subheader("Demo Client Profile")
    _dataframe(st, [client])
    st.subheader("Business Context")
    st.markdown(f"**Business model:** {context['business_model']}")
    st.markdown(f"**Workflow channels:** {', '.join(context['workflow_channels'])}")
    st.markdown(f"**Operating pattern:** {context['current_operating_pattern']}")
    st.markdown(f"**Consulting angle:** {context['consulting_angle']}")


def render_pain_point_diagnosis(st: Any, data: DashboardData) -> None:
    st.header("Pain Point Diagnosis")
    _dataframe(st, pain_point_rows(data), height=260)
    for row in pain_point_rows(data):
        with st.expander(f"{row['id']} - {row['workflow_area']}"):
            st.markdown(f"**Severity:** {row['severity']}")
            st.markdown(f"**Bottleneck:** {row['bottleneck']}")
            st.markdown(f"**Explanation:** {row['impact_summary']}")


def render_opportunity_scorecard(st: Any, data: DashboardData) -> None:
    st.header("Opportunity Scorecard")
    st.caption("Deterministic weighted scoring from synthetic demo pain points.")
    _dataframe(st, opportunity_rows(data), height=280)


def render_useful_signals(st: Any, data: DashboardData) -> None:
    st.header("Useful Signals")
    st.caption("Future AgentHub Useful Signals import candidates. No runtime call is made.")
    _dataframe(st, useful_signal_rows(data), height=280)


def render_recommended_actions(st: Any, data: DashboardData) -> None:
    st.header("Recommended Actions")
    st.caption("All recommendations are no-execution text guidance.")
    _dataframe(st, recommended_action_rows(data), height=280)


def render_report_export(st: Any, data: DashboardData, root: Path | None = None) -> None:
    st.header("Report Export")
    st.caption("Downloads use in-memory public-safe content. File generation writes only to outputs/public_reports/.")
    tab_markdown, tab_json, tab_csv = st.tabs(["Markdown", "JSON", "CSV"])
    with tab_markdown:
        st.download_button(
            "Download Markdown Report",
            data=data.artifacts.markdown,
            file_name="clientdeliverykit_demo_report.md",
            mime="text/markdown",
        )
        st.code(data.artifacts.markdown[:5000], language="markdown")
    with tab_json:
        st.download_button(
            "Download JSON Report",
            data=data.artifacts.json_text,
            file_name="clientdeliverykit_demo_report.json",
            mime="application/json",
        )
        st.code(data.artifacts.json_text[:5000], language="json")
    with tab_csv:
        st.download_button(
            "Download CSV Scorecard",
            data=data.artifacts.csv_text,
            file_name="clientdeliverykit_opportunity_scorecard.csv",
            mime="text/csv",
        )
        st.code(data.artifacts.csv_text, language="csv")
    if st.button("Regenerate Public-Safe Demo Artifacts", type="secondary"):
        paths = generate_public_demo_artifacts(root=root)
        st.success("Demo artifacts regenerated in outputs/public_reports/.")
        for artifact_type, path in paths.items():
            st.markdown(f"- {artifact_type}: `{path}`")


def render_agenthub_integration(st: Any, data: DashboardData) -> None:
    st.header("AgentHub Integration")
    manifest = data.manifest
    st.markdown(f"**Dashboard URL:** {DASHBOARD_URL}")
    st.markdown(f"**Manifest status:** `{manifest.get('status')}`")
    st.markdown(f"**Next recommended action:** `{manifest.get('next_recommended_action')}`")
    st.markdown("**Future integration targets:** Useful Signals, Action Center, Report Export.")
    st.caption("No AgentHub runtime call, connector, or external account connection is used.")
    st.subheader("Connector Readiness")
    _dataframe(st, connector_rows(data), height=300)


def render_dashboard(st: Any, data: DashboardData, root: Path | None = None) -> None:
    st.title("ClientDeliveryKitAgent Consultant Dashboard")
    st.markdown("Local-first AI automation delivery workflow for public-safe demo review.")
    st.warning("Synthetic demo data only. No file upload, no credential input, no live connector.")
    tabs = st.tabs(SECTION_TITLES)
    renderers = [
        render_overview,
        render_client_snapshot,
        render_pain_point_diagnosis,
        render_opportunity_scorecard,
        render_useful_signals,
        render_recommended_actions,
        render_report_export,
        render_agenthub_integration,
    ]
    for tab, renderer in zip(tabs, renderers):
        with tab:
            if renderer is render_report_export:
                renderer(st, data, root=root)
            else:
                renderer(st, data)
