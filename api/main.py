from fastapi import FastAPI
from shared.models import MetricsData, LogBatch
from database.db_manager import save_metrics
from parser.log_parser import parse_logs
from database.db_manager import save_logs

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
    save_metrics(metrics.model_dump())
    return {
        "status": "success"
    }
@app.post("/logs")
def receive_logs(batch: LogBatch):

    raw_logs = []

    for log in batch.logs:
        raw_logs.append(log.message)

    parsed_logs = parse_logs(raw_logs)

    save_logs(parsed_logs)

    return {
        "status": "success",
        "received": len(parsed_logs)
    }