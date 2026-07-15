import time
import requests
import socket
from config import LOG_API_URL
from config import LOG_FILE

def send_log(line):
    payload = {
    "hostname": socket.gethostname(),
    "logs": [
        {
            "message": line.strip()
        }
    ]
    }
    try:

        response = requests.post(
            LOG_API_URL,
            json=payload,
            timeout=5
        )
        print(
            f"Sent Log | Status {response.status_code}"
        )
    except requests.exceptions.RequestException as e:
        print(e)
def start_log_watcher():
    with open(LOG_FILE, "a"):
        pass
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)
        print(f"Watching {LOG_FILE}")
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            send_log(line)

if __name__ == "__main__":

    start_log_watcher()