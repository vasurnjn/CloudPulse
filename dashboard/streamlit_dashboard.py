import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from analytics.metrics_analyzer import(
    get_all_hosts,
    get_latest_metrics,
    get_total_records,
    get_average_cpu,
    get_average_memory,
    get_average_disk,
    get_max_cpu,
    get_max_memory,
    get_max_disk,
    get_min_cpu,
    get_min_memory,
    get_min_disk,
    get_metrics_history
)
from analytics.logs_analyzer import get_latest_logs
from config.settings import LATEST_LOG_LIMIT
from analytics.alerts_analyzer import get_latest_alerts
from config.settings import LATEST_ALERT_LIMIT, COLLECTION_INTERVAL, HISTORY_LIMIT
from datetime import datetime
import pandas as pd


st.set_page_config(
    page_icon="☁️",
    page_title="CloudPulse",
    layout="wide"
)

st.sidebar.title("☁️ CloudPulse")
hosts = ["All"] + get_all_hosts()
selected_host = st.sidebar.selectbox(
    "Select Host",
    hosts
)
st.title("☁️ CloudPulse")
st.subheader("Cloud Infrastructure Monitoring Platform")
st.caption("Real-time Infrastructure Monitoring Dashboard")
st.divider() 

@st.fragment(run_every=f"{COLLECTION_INTERVAL}s")
def live_current_metrics():
    live_metrics = get_latest_metrics(selected_host)

    if live_metrics is None:
        return

    try:
        live_last_update = datetime.fromisoformat(
            live_metrics["timestamp"]
        ).replace(tzinfo=None)
    except Exception:
        try:
            live_last_update = datetime.strptime(
                live_metrics["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )
        except Exception:
            return

    live_age = (
        datetime.now() - live_last_update
    ).total_seconds()

    st.subheader("Current Metrics")
    st.caption(f"🖥️ Monitoring: {selected_host}")

    if live_age <= COLLECTION_INTERVAL * 2:
        st.success(
            f"🟢 CloudPulse Status: Monitoring Active\n\n"
            f"Last Updated (UTC): {live_metrics['timestamp']}"
        )
    else:
        st.warning(
            f"🔴 CloudPulse Status: Monitoring Inactive\n\n"
            f"Showing historical data.\n\n"
            f"Last Updated: {live_metrics['timestamp']}"
        )

    total_records_live = get_total_records(selected_host)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "CPU Usage",
            f"{live_metrics['cpu_usage']:.2f}%"
        )

    with col2:
        st.metric(
            "Memory Usage",
            f"{live_metrics['memory_usage']:.2f}%"
        )

    with col3:
        st.metric(
            "Disk Usage",
            f"{live_metrics['disk_usage']:.2f}%"
        )
    with col4:
        st.metric(
        "Total Records",
        total_records_live
    )

live_current_metrics()
@st.fragment(run_every=f"{COLLECTION_INTERVAL}s")
def live_sidebar():
    sidebar_metrics = get_latest_metrics(selected_host)

    if sidebar_metrics is None:
        st.write("**Status:** 🔴 Inactive")
        return

    try:
        sidebar_last_update = datetime.fromisoformat(
            sidebar_metrics["timestamp"]
        ).replace(tzinfo=None)
    except Exception:
        try:
            sidebar_last_update = datetime.strptime(
                sidebar_metrics["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )
        except Exception:
            return

    sidebar_age = (
        datetime.now() - sidebar_last_update
    ).total_seconds()

    sidebar_status = (
        "🟢 Active"
        if sidebar_age <= COLLECTION_INTERVAL * 2
        else "🔴 Inactive"
    )

    sidebar_records = get_total_records(selected_host)

    st.markdown("### Dashboard Info")
    st.write("**Version:** v2.0.0")
    st.write(f"**Status:** {sidebar_status}")
    st.write(f"**Refresh Interval:** {COLLECTION_INTERVAL} sec")
    st.divider()

    st.markdown("### Database")
    st.write(f"**Records Collected:** {sidebar_records}")
    st.divider()

    st.markdown("### Last Update")
    st.write(sidebar_metrics["timestamp"])

with st.sidebar:
    live_sidebar()

@st.fragment(run_every=f"{COLLECTION_INTERVAL}s")
def live_analytics():

    average_cpu = get_average_cpu(selected_host)
    average_memory = get_average_memory(selected_host)
    average_disk = get_average_disk(selected_host)

    max_cpu = get_max_cpu(selected_host)
    max_memory = get_max_memory(selected_host)
    max_disk = get_max_disk(selected_host)

    min_cpu = get_min_cpu(selected_host)
    min_memory = get_min_memory(selected_host)
    min_disk = get_min_disk(selected_host)

    history = get_metrics_history(
        HISTORY_LIMIT,
        selected_host
    )

    st.divider()
    st.subheader("Analytics")

    cpu_col, memory_col, disk_col = st.columns(3)

    with cpu_col:
        with st.container(border=True):
            st.markdown("### CPU")
            st.write(f"**Average:** {average_cpu:.2f}%")
            st.write(f"**Maximum:** {max_cpu:.2f}%")
            st.write(f"**Minimum:** {min_cpu:.2f}%")

    with memory_col:
        with st.container(border=True):
            st.markdown("### MEMORY")
            st.write(f"**Average:** {average_memory:.2f}%")
            st.write(f"**Maximum:** {max_memory:.2f}%")
            st.write(f"**Minimum:** {min_memory:.2f}%")

    with disk_col:
        with st.container(border=True):
            st.markdown("### DISK")
            st.write(f"**Average:** {average_disk:.2f}%")
            st.write(f"**Maximum:** {max_disk:.2f}%")
            st.write(f"**Minimum:** {min_disk:.2f}%")

    st.divider()

    st.subheader(
        f"Recent History (Last {len(history)} Samples)"
    )

    if history:
        history_df = pd.DataFrame(history)

        st.markdown("### CPU Usage History")
        st.line_chart(
            history_df.set_index("timestamp")["cpu_usage"]
        )

        st.markdown("### Memory Usage History")
        st.line_chart(
            history_df.set_index("timestamp")["memory_usage"]
        )

        st.markdown("### Disk Usage History")
        st.line_chart(
            history_df.set_index("timestamp")["disk_usage"]
        )
    else:
        st.info("No metric history available.")


live_analytics()

@st.fragment(run_every=f"{COLLECTION_INTERVAL}s")
def live_logs_and_alerts():

    st.divider()
    st.subheader("Latest Logs")

    latest_logs = get_latest_logs(LATEST_LOG_LIMIT,selected_host)

    if not latest_logs:
        st.info("No logs available.")
    else:
        for log in latest_logs:
            with st.container(border=True):
                level = log["level"]

                if level == "ERROR":
                    icon = "🔴"
                elif level == "WARNING":
                    icon = "🟡"
                else:
                    icon = "🔵"

                st.write(f"{icon} **{level}**")
                st.caption(log["timestamp"])
                st.write(log["message"])

    st.divider()
    st.subheader("Latest Alerts")

    latest_alerts = get_latest_alerts(LATEST_ALERT_LIMIT,selected_host)

    if not latest_alerts:
        st.success("No recent alerts.")
    else:
        for alert in latest_alerts:
            with st.container(border=True):
                severity = alert["severity"]

                if severity == "HIGH":
                    icon = "🟥"
                elif severity == "ERROR":
                    icon = "🔴"
                else:
                    icon = "🟢"

                st.write(
                    f"{icon} **{severity}** | {alert['source']}"
                )
                st.caption(alert["timestamp"])
                st.write(alert["message"])


live_logs_and_alerts()
st.divider()
st.caption(
    "☁️ CloudPulse v2.0.0 | Built with Python, SQLite, Streamlit & ❤️\n\n"
    "Developed by Vasu Ranjan"
)