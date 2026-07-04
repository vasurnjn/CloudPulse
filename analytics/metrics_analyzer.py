import sqlite3
def run_query(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res=cur.fetchone()
    con.close()
    return res
def run_query_all(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    con.close()
    return res

def get_average_cpu():
    return run_query("SELECT AVG(cpu_usage) FROM system_metrics")[0]

def get_average_memory():
    return run_query("SELECT AVG(memory_usage) FROM system_metrics")[0]

def get_average_disk():
    return run_query("SELECT AVG(disk_usage) FROM system_metrics")[0]

def get_max_cpu():
    return run_query("SELECT MAX(cpu_usage) FROM system_metrics")[0]

def get_max_memory():
    return run_query("SELECT MAX(memory_usage) FROM system_metrics")[0]

def get_max_disk():
    return run_query("SELECT MAX(disk_usage) FROM system_metrics")[0]

def get_min_cpu():
    return run_query("SELECT MIN(cpu_usage) FROM system_metrics")[0]

def get_min_memory():
    return run_query("SELECT MIN(memory_usage) FROM system_metrics")[0]

def get_min_disk():
    return run_query("SELECT MIN(disk_usage) FROM system_metrics")[0] 

def get_total_records():
    return run_query("SELECT COUNT(*) FROM system_metrics")[0]

def get_latest_metrics():
    row = run_query(
        """
        SELECT timestamp,
        cpu_usage,
        memory_usage,
        disk_usage
        FROM system_metrics
        ORDER BY id DESC
        LIMIT 1
        """
    )
    if row is None:
        return None
    return {
        "timestamp": row[0],
        "cpu_usage": row[1],
        "memory_usage": row[2],
        "disk_usage": row[3]
    }

def get_metrics_history(limit):
    rows = run_query_all(
        """
        SELECT timestamp,
        cpu_usage,
        memory_usage,
        disk_usage
        FROM system_metrics
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )
    history = []
    for row in rows:
        history.append({
            "timestamp": row[0],
            "cpu_usage": row[1],
            "memory_usage": row[2],
            "disk_usage": row[3]
        })
    history.reverse()
    return history
