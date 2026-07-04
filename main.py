import time
from dashboard.console_dashboard import display_metrics
from database.db_manager import init_database,save_metrics,save_logs,save_alerts
from collector.metrics_collector import collect_system_metrics
from parser.log_parser import parse_logs
from utils.terminal import clear_terminal
from analytics.metrics_analyzer import get_average_cpu, get_latest_logs, get_max_cpu, get_total_records, get_min_cpu, get_average_memory, get_average_disk, get_max_memory, get_max_disk, get_min_memory, get_min_disk, get_latest_alerts
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
    latest_logs=get_latest_logs(5)

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

    alerts=check_alerts(metrics,parsed_logs)
    save_alerts(alerts)
    latest_alerts=get_latest_alerts(5)
    # latest=get_latest_metrics()
    display_metrics(metrics, average_cpu, max_cpu, total_records, min_cpu, average_memory, max_memory, min_memory, average_disk, max_disk, min_disk,latest_logs,latest_alerts)
    time.sleep(10)