CPU_THRESHOLD=90
MEMORY_THRESHOLD=90
DISK_THRESHOLD=90

def check_alerts(metrics,latest_logs):
    alerts=[]
    if metrics["cpu_usage"]>CPU_THRESHOLD:
        alerts.append({ "timestamp":metrics["timestamp"],
                        "severity":"HIGH",
                      "source":"CPU",
                      "message":f"CPU usage exceeded {CPU_THRESHOLD}%"
                      })
    if metrics["memory_usage"]>MEMORY_THRESHOLD:
        alerts.append({ "timestamp":metrics["timestamp"],
                        "severity":"HIGH",
                      "source":"MEMORY",
                      "message":f"Memory usage exceeded {MEMORY_THRESHOLD}%"
                      })
    if metrics["disk_usage"]>DISK_THRESHOLD:
        alerts.append({ "timestamp":metrics["timestamp"],
                        "severity":"HIGH",
                      "source":"DISK",
                      "message":f"Disk usage exceeded {DISK_THRESHOLD}%"
                      }) 
    for log in latest_logs:
        if log["level"]=="ERROR":
            alerts.append({ "timestamp":log["timestamp"],
                            "severity":"ERROR",
                          "source":"LOG",
                          "message":log["message"]
                          })
    return alerts

