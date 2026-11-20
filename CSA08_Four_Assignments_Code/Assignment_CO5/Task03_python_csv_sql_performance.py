import csv
import io
import random
import sqlite3
import time

def generate_data(stations):
    data = []
    for station_no in range(stations):
        for hour in range(8760):
            day = hour // 24 + 1
            data.append((f"Station{station_no}", day, round(random.uniform(10, 150), 2)))
    return data

def python_method(data):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["station", "day", "pm25"])
    writer.writerows(data)
    output.seek(0)
    totals = {}
    for row in csv.DictReader(output):
        key = (row["station"], int(row["day"]))
        value = float(row["pm25"])
        if key not in totals:
            totals[key] = [0.0, 0]
        totals[key][0] += value
        totals[key][1] += 1
    output.close()
    return {key: round(total / count, 2) for key, (total, count) in totals.items()}

def sql_method(data):
    with sqlite3.connect(":memory:") as con:
        con.execute("CREATE TABLE aq(station TEXT, day INTEGER, pm25 REAL)")
        con.executemany("INSERT INTO aq VALUES (?, ?, ?)", data)
        return con.execute(
            "SELECT station, day, AVG(pm25) FROM aq GROUP BY station, day"
        ).fetchall()

for size in [1, 12, 120]:
    data = generate_data(size)
    print("\nStations:", size)
    print("Total Readings:", len(data))
    start = time.perf_counter()
    result1 = python_method(data)
    python_time = time.perf_counter() - start
    start = time.perf_counter()
    result2 = sql_method(data)
    sql_time = time.perf_counter() - start
    print("Python Loop Time:", round(python_time, 4))
    print("SQL Time:", round(sql_time, 4))
    print("Python groups:", len(result1), "SQL groups:", len(result2))
