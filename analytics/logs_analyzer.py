import sqlite3
def run_query_all(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    con.close()
    return res

def get_latest_logs(limit):
    rows = run_query_all(
        """
        SELECT timestamp, level, message
        FROM application_logs
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )
    latest_logs = []
    for row in rows:
        latest_logs.append(
            {
                "timestamp": row[0],
                "level": row[1],
                "message": row[2]
            }
        )
    latest_logs.reverse()
    return latest_logs