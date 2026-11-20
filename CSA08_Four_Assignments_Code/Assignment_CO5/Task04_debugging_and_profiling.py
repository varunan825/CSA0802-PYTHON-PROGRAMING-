import cProfile
import logging
import time
from collections import defaultdict

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(filename)s:%(lineno)d:%(message)s"
)
logging.info("Starting sample air-quality analysis")

readings = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0),
    ("Guindy", "2026-10-03", 121.0),
    ("Adyar", "2026-10-04", 60.0)
]

def daily_means(rows):
    totals = defaultdict(lambda: [0.0, 0])
    for station, day, pm25 in rows:
        assert pm25 >= 0, "PM2.5 must be non-negative"
        key = (station, day)
        totals[key][0] += pm25
        totals[key][1] += 1
    return {key: total / count for key, (total, count) in totals.items()}

start = time.perf_counter()
summary = daily_means(readings)
elapsed = time.perf_counter() - start
print("Daily means:", summary)
print("Elapsed seconds:", elapsed)

print("\nProfiler summary:")
cProfile.run("daily_means(readings)")
