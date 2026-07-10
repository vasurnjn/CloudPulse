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