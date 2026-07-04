from config.settings import (
    COLLECTION_INTERVAL,
    LATEST_LOG_LIMIT,
    LATEST_ALERT_LIMIT
)
import time
from dashboard.console_dashboard import display_metrics
from database.db_manager import init_database,save_metrics,save_logs,save_alerts
from collector.metrics_collector import collect_system_metrics
from parser.log_parser import parse_logs
from utils.terminal import clear_terminal
from analytics.metrics_analyzer import (
    get_average_cpu,
    get_average_memory, 
    get_average_disk, 
    get_max_cpu, 
    get_max_disk, 
    get_max_memory, 
    get_min_cpu, 
    get_min_memory, 
    get_min_disk, 
    get_total_records
)
from analytics.logs_analyzer import get_latest_logs
from analytics.alerts_analyzer import get_latest_alerts
from collector.log_collector import collect_application_logs
from alerts.alert_engine import check_alerts

init_database()
while True:
    clear_terminal()
    metrics=collect_system_metrics()
    save_metrics(metrics)

    raw_logs=collect_application_logs()
    parsed_logs=parse_logs(raw_logs)
    save_logs(parsed_logs)
    latest_logs=get_latest_logs(LATEST_LOG_LIMIT)

    average_cpu=get_average_cpu()
    average_memory=get_average_memory()
    average_disk=get_average_disk()

    max_cpu=get_max_cpu()
    max_memory=get_max_memory()
    max_disk=get_max_disk()

    min_cpu=get_min_cpu()
    min_memory=get_min_memory()
    min_disk=get_min_disk()

    total_records=get_total_records()
    analytics_summary={
    "cpu": {
        "average": average_cpu,
        "maximum": max_cpu,
        "minimum": min_cpu
    },
    "memory": {
        "average": average_memory,
        "maximum": max_memory,
        "minimum": min_memory
    },
    "disk": {
        "average": average_disk,
        "maximum": max_disk,
        "minimum": min_disk
    },
    "total_records": total_records
}

    alerts=check_alerts(metrics,parsed_logs)
    save_alerts(alerts)
    latest_alerts=get_latest_alerts(LATEST_ALERT_LIMIT)
    # latest=get_latest_metrics()
    display_metrics(
    metrics,
    analytics_summary,
    latest_logs,
    latest_alerts
)
    time.sleep(COLLECTION_INTERVAL)