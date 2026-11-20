trains = {
    101: {"name": "Chennai Express",
          "stations": [("Chennai", "06:00", "06:10"), ("Katpadi", "08:00", "08:05"), ("Bangalore", "11:00", "11:10")],
          "days": {"Monday", "Tuesday", "Wednesday"}},
    102: {"name": "Pandian Express",
          "stations": [("Chennai", "07:00", "07:10"), ("Villupuram", "09:00", "09:05"), ("Madurai", "13:00", "13:10")],
          "days": {"Monday", "Friday"}},
    103: {"name": "Coimbatore Express",
          "stations": [("Chennai", "08:00", "08:10"), ("Salem", "11:00", "11:05"), ("Coimbatore", "14:00", "14:10")],
          "days": {"Tuesday", "Thursday"}},
    104: {"name": "Mysore Express",
          "stations": [("Chennai", "09:00", "09:10"), ("Katpadi", "11:00", "11:05"), ("Mysore", "15:00", "15:10")],
          "days": {"Monday", "Wednesday"}},
    105: {"name": "Kanyakumari Express",
          "stations": [("Chennai", "10:00", "10:10"), ("Villupuram", "12:00", "12:05"), ("Kanyakumari", "18:00", "18:10")],
          "days": {"Friday", "Saturday"}}
}

print("RAILWAY TIMETABLE")
for number, details in trains.items():
    print("\nTrain Number:", number)
    print("Train Name:", details["name"])
    print("Running Days:", sorted(details["days"]))
    for station, arrival, departure in details["stations"]:
        print(station, arrival, departure)

search_station, search_day = "Katpadi", "Monday"
results = []
for number, details in trains.items():
    if search_day in details["days"]:
        for station, arrival, departure in details["stations"]:
            if station == search_station:
                results.append((number, details["name"], arrival, departure))
results.sort(key=lambda item: item[3])
print("\nTrains stopping at", search_station, "on", search_day)
for train in results:
    print(train)

station_index = {}
for number, details in trains.items():
    for station, arrival, departure in details["stations"]:
        station_index.setdefault(station, []).append(number)
print("\nStation Index:", station_index)
print("Third Station Departure:", trains[101]["stations"][2][2])
