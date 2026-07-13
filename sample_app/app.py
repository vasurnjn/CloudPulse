import random
import time
from datetime import datetime

LOG_FILE = "sample_app/app.log"

messages = [
    ("INFO", "User logged in"),
    ("INFO", "Dashboard opened"),
    ("INFO", "Request completed"),
    ("WARNING", "High response time detected"),
    ("WARNING", "Memory usage increasing"),
    ("ERROR", "Database connection failed"),
    ("ERROR", "Request timeout"),
]


while True:

    level, message = random.choice(messages)

    log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {level} {message}"

    with open(LOG_FILE, "a") as file:
        file.write(log + "\n")

    print(log)

    time.sleep(random.randint(3, 8))