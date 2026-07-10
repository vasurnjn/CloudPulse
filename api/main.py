from fastapi import FastAPI
from shared.models import MetricsData
from database.db_manager import save_metrics

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