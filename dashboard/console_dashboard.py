
def display_metrics(
    metrics,
    analytics_summary,
    latest_logs,
    latest_alerts
):
    network=metrics['network_usage']
    memory=metrics['memory_usage']
    print("========================================")
    print("CloudPulse v0.8")
    print("========================================")
    print()
    print("System Information")
    print("------------------")
    print(f"Hostname: {metrics['hostname']}")
    print(f"Time:     {metrics['timestamp']}")
    print()
    print("Current Metrics")
    print("---------------")
    print(f"CPU Usage:     {metrics['cpu_usage']}%")
    print(f"Memory Usage:  {memory}%")
    print(f"Disk Usage:    {metrics['disk_usage']}%")
    print()
    print("Analytics")
    print("---------")
    print(f"Average CPU Usage:  {analytics_summary['cpu']['average']:.2f}%")
    print(f"Maximum CPU Usage:  {analytics_summary['cpu']['maximum']:.2f}%")
    print(f"Minimum CPU Usage:  {analytics_summary['cpu']['minimum']:.2f}%")
    print()
    print(f"Average Memory Usage:  {analytics_summary['memory']['average']:.2f}%")
    print(f"Maximum Memory Usage:  {analytics_summary['memory']['maximum']:.2f}%")
    print(f"Minimum Memory Usage:  {analytics_summary['memory']['minimum']:.2f}%")
    print()
    print(f"Average Disk Usage: {analytics_summary['disk']['average']:.2f}%")
    print(f"Maximum Disk Usage: {analytics_summary['disk']['maximum']:.2f}%")
    print(f"Minimum Disk Usage: {analytics_summary['disk']['minimum']:.2f}%")
    print()
    print(f"Total Records Collected: {analytics_summary['total_records']}")
    print()
    print("Network")
    print("-------")
    print(f"Bytes Sent:     {network['bytes_sent']}")
    print(f"Bytes Received: {network['bytes_recv']}")
    print()
    # print()
    # print(f"Last Updated: {metrics['timestamp']}")
    print("========================================")
    print()
    print("Latest Logs")
    print("-----------")
    if not latest_logs:
        print("No logs stored.")
    else:
        for log in latest_logs:
            print(f"[{log['level']}] {log['timestamp']}")
            print(f"{log['message']}")
            print()
    print("Latest Alerts")
    print("-------------")
    if not latest_alerts:
        print("No alerts to display.")
    else:
        for alert in latest_alerts:
            print(f"[{alert['timestamp']}]")
            print(f"[{alert['severity']}] {alert['source']}")
            print(f"{alert['message']}")
            print()