from pathlib import Path

from client_delivery_kit import dashboard_views


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_dashboard_sections_match_required_page_structure():
    assert dashboard_views.SECTION_TITLES == [
        "Overview",
        "Client Snapshot",
        "Pain Point Diagnosis",
        "Opportunity Scorecard",
        "Useful Signals",
        "Recommended Actions",
        "Report Export",
        "AgentHub Integration",
    ]


def test_dashboard_views_expose_public_safe_disclaimer():
    source = (PROJECT_ROOT / "client_delivery_kit" / "dashboard_views.py").read_text(encoding="utf-8")

    assert "Synthetic demo data only" in source
    assert "no live connector" in source
    assert "Regenerate Public-Safe Demo Artifacts" in source


def test_dashboard_views_do_not_include_upload_or_credential_inputs():
    source = (PROJECT_ROOT / "client_delivery_kit" / "dashboard_views.py").read_text(encoding="utf-8")
    forbidden_terms = [
        "file_uploader",
        "camera_input",
        "chat_input",
        "text_input",
        "text_area",
        "number_input",
        "connect_real_connector",
    ]

    assert [term for term in forbidden_terms if term in source] == []
