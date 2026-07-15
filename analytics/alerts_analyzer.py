import sqlite3
def run_query_all(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    con.close()
    return res

def get_latest_alerts(limit, hostname=None):
    query = """
        SELECT timestamp, hostname, severity, source, message
        FROM alerts
    """
    params = []
    if hostname and hostname != "All":
        query += " WHERE hostname = ?"
        params.append(hostname)
    query += """
        ORDER BY id DESC
        LIMIT ?
    """
    params.append(limit)
    rows = run_query_all(
        query,
        tuple(params)
    )
    latest_alerts = []
    for row in rows:
        latest_alerts.append(
            {
                "timestamp": row[0],
                "hostname": row[1],
                "severity": row[2],
                "source": row[3],
                "message": row[4]
            }
        )
    latest_alerts.reverse()
    return latest_alerts