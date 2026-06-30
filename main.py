import time
from dashboard.console_dashboard import display_metrics
from database.db_manager import init_database,save_metrics
from collector.metrics_collector import collect_system_metrics
from utils.terminal import clear_terminal
init_database()
while True:
    metrics=collect_system_metrics()
    save_metrics(metrics)
    clear_terminal()
    display_metrics(metrics)
    time.sleep(10)