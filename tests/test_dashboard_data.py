from pathlib import Path

from client_delivery_kit.dashboard_data import (
    CURRENT_CHECKPOINT,
    DASHBOARD_URL,
    expected_public_artifact_paths,
    generate_public_demo_artifacts,
    load_dashboard_data,
    opportunity_rows,
    pain_point_rows,
    recommended_action_rows,
    useful_signal_rows,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_load_dashboard_data_returns_consultant_demo_counts():
    data = load_dashboard_data(root=PROJECT_ROOT)

    assert data.report.client_snapshot.company_label == "Demo Local Services Co."
    assert data.overview_metrics["opportunities"] == 4
    assert data.overview_metrics["useful_signals"] == 4
    assert data.overview_metrics["recommended_actions"] == 4
    assert data.top_opportunity["opportunity_id"] == "opp_001"
    assert CURRENT_CHECKPOINT.endswith("COMPLETE")
    assert DASHBOARD_URL == "http://localhost:8535"


def test_dashboard_rows_are_table_ready_and_no_execution():
    data = load_dashboard_data(root=PROJECT_ROOT)

    assert len(pain_point_rows(data)) == 4
    assert len(opportunity_rows(data)) == 4
    assert len(useful_signal_rows(data)) == 4
    actions = recommended_action_rows(data)
    assert len(actions) == 4
    assert {row["execution_mode"] for row in actions} == {"template_only"}


def test_expected_public_artifact_paths_are_under_public_reports():
    paths = expected_public_artifact_paths(root=PROJECT_ROOT)

    assert set(paths) == {"markdown", "json", "csv"}
    assert all(path.parent.name == "public_reports" for path in paths.values())


def test_generate_public_demo_artifacts_refreshes_only_public_reports():
    paths = generate_public_demo_artifacts(root=PROJECT_ROOT)

    assert set(paths) == {"markdown", "json", "csv"}
    assert all(path.exists() for path in paths.values())
    assert all(path.parent.name == "public_reports" for path in paths.values())
