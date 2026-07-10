import sqlite3

def run_query(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res = cur.fetchone()
    con.close()
    return res

def run_query_all(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    con.close()
    return res

def get_all_hosts():
    rows = run_query_all("""
        SELECT DISTINCT hostname
        FROM system_metrics
        WHERE hostname IS NOT NULL
        AND hostname != ''
        AND hostname != 'string'
        ORDER BY hostname
        """)
    return [row[0] for row in rows]

def aggregate(function, column, hostname=None):
    query = f"SELECT {function}({column}) FROM system_metrics"
    params = ()
    if hostname and hostname != "All":
        query += " WHERE hostname=?"
        params = (hostname,)
    result = run_query(query, params)[0]
    return result if result is not None else 0


def get_average_cpu(hostname=None):
    return aggregate("AVG", "cpu_usage", hostname)

def get_average_memory(hostname=None):
    return aggregate("AVG", "memory_usage", hostname)

def get_average_disk(hostname=None):
    return aggregate("AVG", "disk_usage", hostname)

def get_max_cpu(hostname=None):
    return aggregate("MAX", "cpu_usage", hostname)

def get_max_memory(hostname=None):
    return aggregate("MAX", "memory_usage", hostname)

def get_max_disk(hostname=None):
    return aggregate("MAX", "disk_usage", hostname)

def get_min_cpu(hostname=None):
    return aggregate("MIN", "cpu_usage", hostname)

def get_min_memory(hostname=None):
    return aggregate("MIN", "memory_usage", hostname)

def get_min_disk(hostname=None):
    return aggregate("MIN", "disk_usage", hostname)


def get_total_records(hostname=None):
    query = "SELECT COUNT(*) FROM system_metrics"
    params = ()
    if hostname and hostname != "All":
        query += " WHERE hostname=?"
        params = (hostname,)
    return run_query(query, params)[0]

def get_latest_metrics(hostname=None):
    query = """
        SELECT
            timestamp,
            hostname,
            cpu_usage,
            memory_usage,
            disk_usage
        FROM system_metrics
    """
    params = ()
    if hostname and hostname != "All":
        query += " WHERE hostname=?"
        params = (hostname,)
    query += """
        ORDER BY id DESC
        LIMIT 1
    """
    row = run_query(query, params)
    if row is None:
        return None
    return {
        "timestamp": row[0],
        "hostname": row[1],
        "cpu_usage": row[2],
        "memory_usage": row[3],
        "disk_usage": row[4]
    }

def get_metrics_history(limit, hostname=None):
    query = """
        SELECT
            timestamp,
            cpu_usage,
            memory_usage,
            disk_usage
        FROM system_metrics
    """
    params = ()
    if hostname and hostname != "All":
        query += " WHERE hostname=?"
        params = (hostname,)
    query += """
        ORDER BY id DESC
        LIMIT ?
    """
    params = params + (limit,)
    rows = run_query_all(query, params)
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