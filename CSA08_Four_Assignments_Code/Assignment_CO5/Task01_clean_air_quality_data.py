import csv
import io
import sqlite3

RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Chennai,2026-10-04,1200
"""

def load_clean(text):
    rows = []
    for row in csv.DictReader(io.StringIO(text)):
        value = (row.get("pm25") or "").strip()
        if not value or value.upper() == "NA":
            continue
        try:
            pm = float(value)
        except ValueError:
            continue
        if pm < 0 or pm > 999:
            continue
        rows.append((row["station"].strip(), row["date"].strip(), pm))
    return rows

def min_max(values):
    if not values:
        return []
    minimum, maximum = min(values), max(values)
    if minimum == maximum:
        return [0.0] * len(values)
    return [round((value - minimum) / (maximum - minimum), 3) for value in values]

clean = load_clean(RAW)
print("CLEANED DATA")
for row in clean:
    print(row)
print("\nNORMALISED DATA")
print(min_max([pm for _, _, pm in clean]))

with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE readings(station TEXT, date TEXT, pm25 REAL)")
    con.executemany("INSERT INTO readings VALUES (?, ?, ?)", clean)
    print("\nAVERAGE PM2.5")
    print(con.execute("SELECT AVG(pm25) FROM readings WHERE station=?", ("Adyar",)).fetchone()[0])
    print("\nMAXIMUM PM2.5")
    print(con.execute("SELECT MAX(pm25) FROM readings").fetchone()[0])
    print("\nTOTAL READINGS")
    print(con.execute("SELECT COUNT(*) FROM readings").fetchone()[0])
