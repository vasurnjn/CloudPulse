from fastapi import FastAPI

from shared.models import MetricsData, LogBatch
from database.db_manager import save_metrics, save_logs, save_alerts
from parser.log_parser import parse_logs
from alerts.alert_engine import check_alerts

app = FastAPI(
    title="CloudPulse API",
    version="2.0"
)

@app.get("/")
def home():
    return {
        "message": "CloudPulse API Running"
    }

@app.post("/metrics")
def receive_metrics(metrics: MetricsData):
    metrics_data = metrics.model_dump()
    save_metrics(metrics_data)
    alerts = check_alerts(metrics_data, [])
    save_alerts(alerts)
    return {
        "status": "success"
    }

@app.post("/logs")
def receive_logs(batch: LogBatch):
    raw_logs = []
    for log in batch.logs:
        raw_logs.append(log.message)
    parsed_logs = parse_logs(raw_logs)

    for log in parsed_logs:
        log["hostname"] = batch.hostname
    save_logs(parsed_logs, batch.hostname)
    alerts = check_alerts({}, parsed_logs)
    save_alerts(alerts)

    return {
        "status": "success",
        "received": len(parsed_logs)
    }