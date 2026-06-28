"""Streamlit entrypoint for the ClientDeliveryKitAgent consultant dashboard."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from client_delivery_kit.dashboard_data import load_dashboard_data
from client_delivery_kit.dashboard_views import render_dashboard


PROJECT_ROOT = Path(__file__).resolve().parent


def main() -> None:
    st.set_page_config(
        page_title="ClientDeliveryKitAgent",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    data = load_dashboard_data(root=PROJECT_ROOT)
    render_dashboard(st, data, root=PROJECT_ROOT)


if __name__ == "__main__":
    main()
