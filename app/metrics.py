import psutil
import os
import time
from datetime import timedelta

PROCFS = os.getenv("PROCFS_PATH", "/proc")
psutil.PROCFS_PATH = PROCFS

def get_uptime():
    boot = psutil.boot_time()
    seconds = int(time.time() - boot)
    delta = timedelta(seconds=seconds)

    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, _ = divmod(rem, 60)

    human = f"{days}d {hours}h {minutes}m"
    return seconds, human


def get_cpu_temp_avg():
    temps = psutil.sensors_temperatures()
    values = []

    for entries in temps.values():
        for e in entries:
            if e.current is not None:
                values.append(e.current)

    if not values:
        return None

    return round(sum(values) / len(values), 1)


def collect_metrics():
    uptime_sec, uptime_human = get_uptime()

    return {
        "uptime_seconds": uptime_sec,
        "uptime_human": uptime_human,
        "cpu": {
            "percent": psutil.cpu_percent(interval=0.1),
            "load_1m": psutil.getloadavg()[0]
        },
        "ram": {
            "used_mb": int(psutil.virtual_memory().used / 1024 / 1024),
            "total_mb": int(psutil.virtual_memory().total / 1024 / 1024),
            "percent": psutil.virtual_memory().percent
        },
        "temperature": {
            "cpu_avg": get_cpu_temp_avg()
        }
    }
