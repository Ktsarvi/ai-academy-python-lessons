import os
from datetime import datetime

LOG_FILE = "inventory_log.txt"

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", encoding="utf-8"):
        pass

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(f"{timestamp} - Inventory checked")

print("Inventory check logged.")