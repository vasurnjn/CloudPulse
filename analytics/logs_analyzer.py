import sqlite3
def run_query_all(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    con.close()
    return res

def get_latest_logs(limit, hostname=None):
    query = """
        SELECT timestamp, hostname, level, message
        FROM application_logs
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
    latest_logs = []
    for row in rows:
        latest_logs.append(
            {
                "timestamp": row[0],
                "hostname": row[1],
                "level": row[2],
                "message": row[3]
            }
        )
    latest_logs.reverse()
    return latest_logs