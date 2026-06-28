import psutil
from datetime import datetime
import socket
def collect_system_metrics():
    network=psutil.net_io_counters()
    memory=psutil.virtual_memory()
    metrics={
        "cpu_usage":psutil.cpu_percent(interval=1),
        "memory_usage":memory.percent,
        "disk_usage":psutil.disk_usage('C:\\').percent,
        "network_usage": {
            "bytes_sent": network.bytes_sent,
            "bytes_recv": network.bytes_recv
        },
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "hostname": socket.gethostname()
    }
    return metrics