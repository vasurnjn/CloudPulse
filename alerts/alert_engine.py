from config.settings import (
    CPU_THRESHOLD,
    MEMORY_THRESHOLD,
    DISK_THRESHOLD
)

def check_alerts(metrics,latest_logs):
    alerts=[]
    if metrics and metrics["cpu_usage"]>CPU_THRESHOLD:
        alerts.append({ "timestamp":metrics["timestamp"],
                       "hostname": metrics["hostname"],
                        "severity":"HIGH",
                      "source":"CPU",
                      "message":f"CPU usage exceeded {CPU_THRESHOLD}%"
                      })
    if metrics and metrics["memory_usage"]>MEMORY_THRESHOLD:
        alerts.append({ "timestamp":metrics["timestamp"],
                       "hostname": metrics["hostname"],
                        "severity":"HIGH",
                      "source":"MEMORY",
                      "message":f"Memory usage exceeded {MEMORY_THRESHOLD}%"
                      })
    if metrics and metrics["disk_usage"]>DISK_THRESHOLD:
        alerts.append({ "timestamp":metrics["timestamp"],
                       "hostname": metrics["hostname"],
                        "severity":"HIGH",
                      "source":"DISK",
                      "message":f"Disk usage exceeded {DISK_THRESHOLD}%"
                      }) 
    for log in latest_logs:
        if log["level"]=="ERROR":
            alerts.append({ "timestamp":log["timestamp"],
                           "hostname": log["hostname"],
                            "severity":"ERROR",
                          "source":"LOG",
                          "message":log["message"]
                          })
    return alerts

