import sqlite3
def init_database():
    con=sqlite3.connect('database/cloudpulse.db')
    cur=con.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS system_metrics 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                timestamp TEXT, 
                hostname TEXT, 
                cpu_usage REAL, 
                memory_usage REAL, 
                disk_usage REAL, 
                bytes_sent INTEGER, 
                bytes_recv INTEGER)
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS log_offsets
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                filename TEXT UNIQUE, 
                offset INTEGER DEFAULT 0)
                """)
    con.commit()
    con.close()
def save_metrics(metrics):
    network=metrics['network_usage']
    con=sqlite3.connect('database/cloudpulse.db')
    cur=con.cursor()
    cur.execute("""
                INSERT INTO system_metrics (timestamp, hostname, cpu_usage, memory_usage, disk_usage, bytes_sent, bytes_recv)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, 
                (metrics['timestamp'],
                metrics['hostname'],
                metrics['cpu_usage'],
                metrics['memory_usage'],
                metrics['disk_usage'],
                network['bytes_sent'],
                network['bytes_recv'])
    )
    con.commit()
    con.close()

def get_log_offset(filename):
    con=sqlite3.connect("database/cloudpulse.db")
    cur=con.cursor()
    cur.execute("SELECT offset FROM log_offsets WHERE filename=?",(filename,))
    res=cur.fetchone()
    con.close()
    return res[0] if res else 0

def save_log_offset(filename,offset):
    con=sqlite3.connect("database/cloudpulse.db")
    cur=con.cursor()
    cur.execute("INSERT OR REPLACE INTO log_offsets (filename, offset) VALUES (?, ?)", (filename, offset))
    con.commit()
    con.close()