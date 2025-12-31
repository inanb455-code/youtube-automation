import shutil
import os

MIN_FREE_DISK_GB = 5

REQUIRED_DIRS = [
    "output",
    "temp"
]

def run():
    total, used, free = shutil.disk_usage("/")
    free_gb = free / (1024 ** 3)

    if free_gb < MIN_FREE_DISK_GB:
        return False, f"Low disk space: {free_gb:.2f} GB left"

    for d in REQUIRED_DIRS:
        if not os.path.exists(d):
            try:
                os.makedirs(d)
            except Exception as e:
                return False, f"Cannot create directory {d}: {e}"

    return True, "System healthy"
