import os
import socket
import time
from datetime import datetime, UTC
import psutil
import requests
from config import API_URL
from config import SEND_INTERVAL

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
        response = requests.post(API_URL, json=data, timeout=5)
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"Sent | Status {response.status_code}"
        )
    except requests.exceptions.RequestException as e:
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"Connection Failed : {e}"
        )

def start_agent():
    print()
    print("=" * 45)
    print("CloudPulse Agent Started")
    print("=" * 45)
    print(f"Server : {API_URL}")
    print(f"Interval : {SEND_INTERVAL} seconds")
    print()
    while True:
        send_metrics()
        time.sleep(SEND_INTERVAL)

if __name__ == "__main__":
    start_agent()