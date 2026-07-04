import sqlite3
def run_query_all(query, params=()):
    con = sqlite3.connect("database/cloudpulse.db")
    cur = con.cursor()
    cur.execute(query, params)
    res = cur.fetchall()
    con.close()
    return res

def get_latest_alerts(limit):
    rows = run_query_all(
        """
        SELECT timestamp,severity,source,message
        FROM alerts
        ORDER BY id DESC
        LIMIT ?
        """
        ,(limit,)
    )
    latest_alerts=[]
    for row in rows:
        latest_alerts.append(
            {
                "timestamp": row[0],
                "severity": row[1],
                "source": row[2],
                "message": row[3]
            }
        )
    latest_alerts.reverse()
    return latest_alerts