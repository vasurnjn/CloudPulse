from database.db_manager import get_log_offset, save_log_offset

def collect_application_logs():
    LOG_FILE = "logs/sample.log"
    try:
        with open(LOG_FILE,"r") as f:
            offset=get_log_offset(LOG_FILE)
            f.seek(offset)
            logs=f.read().splitlines()
            new_offset=f.tell()
            save_log_offset(LOG_FILE,new_offset)
        return logs
    except FileNotFoundError:
        return []
