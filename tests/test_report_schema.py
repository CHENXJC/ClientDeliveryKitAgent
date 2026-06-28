from client_delivery_kit.report_schema import (
    PUBLIC_SAFE_DISCLAIMER,
    REPORT_ID,
    REPORT_SCHEMA_VERSION,
    build_validation_snapshot,
)


def test_validation_snapshot_contains_public_safe_export_contract():
    snapshot = build_validation_snapshot()

    assert snapshot.export_policy == "outputs/public_reports only"
    assert snapshot.safety_disclaimer == PUBLIC_SAFE_DISCLAIMER
    assert REPORT_ID == "clientdeliverykit_demo_delivery_report"
    assert REPORT_SCHEMA_VERSION == "clientdeliverykit.report.v1"
