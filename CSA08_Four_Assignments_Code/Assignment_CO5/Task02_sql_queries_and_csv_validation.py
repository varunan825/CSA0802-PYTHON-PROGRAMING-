import csv
import io
import sqlite3

readings = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0),
    ("Guindy", "2026-10-03", 121.0),
    ("Adyar", "2026-10-04", 60.0)
]
with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE aq(station TEXT, day TEXT, pm25 REAL)")
    con.executemany("INSERT INTO aq VALUES (?, ?, ?)", readings)

    def station_average(name):
        result = con.execute(
            "SELECT AVG(pm25) FROM aq WHERE station = ?", (name,)
        ).fetchone()
        return result[0]

    print("DATABASE RESULTS")
    print(station_average("Adyar"), station_average("Guindy"))
    print("SQL INJECTION TEST")
    print(station_average("Adyar' OR '1'='1"))

tests = {
    "Correct file": "station,date,pm25\nAdyar,2026-10-01,48",
    "Missing column": "station,date\nAdyar,2026-10-01",
    "Wrong delimiter": "station;date;pm25\nAdyar;2026-10-01;48",
    "Empty file": "",
    "Invalid number": "station,date,pm25\nAdyar,2026-10-01,abc"
}
print("\nFILE VALIDATION")
for name, content in tests.items():
    print("\n" + name)
    try:
        reader = csv.DictReader(io.StringIO(content))
        if not reader.fieldnames:
            raise ValueError("Empty file")
        required = {"station", "date", "pm25"}
        if not required.issubset(set(reader.fieldnames)):
            raise ValueError("Missing column or wrong delimiter")
        for row in reader:
            float(row["pm25"])
        print("Valid file")
    except (ValueError, TypeError) as error:
        print("Rejected:", error)
