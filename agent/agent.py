import threading
import time
import os
import socket
from datetime import datetime, UTC
import psutil
import requests
from config import API_URL
from config import SEND_INTERVAL
from log_watcher import start_log_watcher

def collect_metrics():
    network = psutil.net_io_counters()
    disk_path = os.path.abspath(os.sep)
    return {
        "hostname": socket.gethostname(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage(disk_path).percent,
        "network_usage": {
            "bytes_sent": network.bytes_sent,
            "bytes_recv": network.bytes_recv
        },
        "timestamp": datetime.now(UTC).isoformat()
    }

def send_metrics():
    data = collect_metrics()
    try:
        response = requests.post(
            API_URL,
            json=data,
            timeout=5
        )
        print(
            f"[Metrics] {response.status_code}"
        )
    except requests.exceptions.RequestException as e:
        print(e)

def metrics_loop():
    while True:
        send_metrics()
        time.sleep(SEND_INTERVAL)

def start_agent():
    print("=" * 50)
    print("CloudPulse Agent")
    print("=" * 50)
    metrics_thread = threading.Thread(
        target=metrics_loop,
        daemon=True
    )
    log_thread = threading.Thread(
        target=start_log_watcher,
        daemon=True
    )
    metrics_thread.start()
    log_thread.start()

    metrics_thread.join()
    log_thread.join()

if __name__ == "__main__":
    start_agent()