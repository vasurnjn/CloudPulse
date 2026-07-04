import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from analytics.metrics_analyzer import(
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
st_autorefresh(interval=10000,key="cloudpulse_refresh")
st.title("☁️ CloudPulse")
st.subheader("Cloud Infrastructure Monitoring Platform")
st.caption("Real-time Infrastructure Monitoring Dashboard")
st.divider() 
st.subheader("Current Metrics")
latest_metrics=get_latest_metrics()
if latest_metrics is None:
    st.warning("No metrics available. Start CloudPulse (main.py) first.")
    st.stop()
history=get_metrics_history(HISTORY_LIMIT)
last_update=datetime.strptime(latest_metrics["timestamp"], "%Y-%m-%d %H:%M:%S")
current_time=datetime.now()
age=(current_time-last_update).total_seconds()
if age <= COLLECTION_INTERVAL*2:
    st.success(
        f"🟢 CloudPulse Status: Monitoring Active\n\n"
        f"Last Updated: {latest_metrics['timestamp']}"
    )
else:
    st.warning(
        f"🔴 CloudPulse Status: Monitoring Inactive\n\n"
        f"Showing historical data.\n\n"
        f"Last Updated: {latest_metrics['timestamp']}"
    )
total_records=get_total_records()

st.sidebar.title("☁️ CloudPulse")
st.sidebar.markdown("### Dashboard Info")
st.sidebar.write("**Version:** v0.9")
status = "🟢 Active" if age <= COLLECTION_INTERVAL * 2 else "🔴 Inactive"
st.sidebar.write(f"**Status:** {status}")
st.sidebar.write(f"**Refresh Interval:** {COLLECTION_INTERVAL} sec")
st.sidebar.divider()
st.sidebar.markdown("### Database")
st.sidebar.write(f"**Records Collected:** {total_records}")
st.sidebar.divider()
st.sidebar.markdown("### Last Update")
st.sidebar.write(latest_metrics["timestamp"])

average_cpu=get_average_cpu()
average_memory=get_average_memory()
average_disk=get_average_disk()

max_cpu=get_max_cpu()
max_memory=get_max_memory()
max_disk=get_max_disk()

min_cpu=get_min_cpu()
min_memory=get_min_memory()
min_disk=get_min_disk()
col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric(
        label="CPU Usage",
        value=f"{latest_metrics['cpu_usage']:.2f}%"
    )
with col2:
    st.metric(
        label="Memory Usage",
        value=f"{latest_metrics['memory_usage']:.2f}%"

    )
with col3:
    st.metric(
        label="Disk Usage",
        value=f"{latest_metrics['disk_usage']:.2f}%"

    )
with col4:
    st.metric(
        label="Total Records",
        value=total_records
    )
st.divider()
st.subheader("Analytics")
cpu_col,memory_col,disk_col=st.columns(3)
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
st.subheader(f"Recent History (Last {len(history)} Samples)")
history_df=pd.DataFrame(history)
st.markdown("### CPU Usage History")
st.line_chart(history_df.set_index("timestamp")["cpu_usage"])
st.markdown("### Memory Usage History")
st.line_chart(history_df.set_index("timestamp")["memory_usage"])
st.markdown("### Disk Usage History")
st.line_chart(history_df.set_index("timestamp")["disk_usage"])


st.divider()
st.subheader("Latest Logs")
latest_logs=get_latest_logs(LATEST_LOG_LIMIT)
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
            st.caption(log['timestamp'])
            st.write(log['message'])
st.divider()
st.subheader("Latest Alerts")
latest_alerts=get_latest_alerts(LATEST_ALERT_LIMIT)
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
            st.write(f"{icon} **{severity}** | {alert['source']}")
            st.caption(alert['timestamp'])
            st.write(alert['message'])
st.divider()
st.caption(
    "☁️ CloudPulse v0.9 | Built with Python, SQLite, Streamlit & ❤️\n\n"
    "Developed by Vasu Ranjan"
)