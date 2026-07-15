from pydantic import BaseModel

class NetworkUsage(BaseModel):
    bytes_sent: int
    bytes_recv: int

class MetricsData(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_usage: NetworkUsage
    timestamp: str
    hostname: str
from typing import List
class LogData(BaseModel):
    message: str
class LogBatch(BaseModel):
    hostname: str
    logs: List[LogData]