from collector.metrics_collector import collect_system_metrics 
def display_metrics():
    metrics=collect_system_metrics()
    network=metrics['network_usage']
    memory=metrics['memory_usage']
    print("========================================")
    print("CloudPulse v0.1")
    print("========================================")
    print("System Metrics Collected:")
    print(f"Hostname: {metrics['hostname']}")
    print(f"Time: {metrics['timestamp']}")
    print()
    print(f"CPU Usage: {metrics['cpu_usage']}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {metrics['disk_usage']}%")
    print()
    print("Network Usage:")
    print(f"Bytes Sent: {network['bytes_sent']}")
    print(f"Bytes Received: {network['bytes_recv']}")
    print("========================================")