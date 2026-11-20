readings = [2, 5, 9, 12, -60, 4, 55, 7, 3, -5]

valid = []
fahrenheit = []
for celsius in readings:
    if -50 <= celsius <= 50:
        valid.append(celsius)
        fahrenheit.append(celsius * 9 / 5 + 32)
print("Valid Celsius:", valid)
print("Fahrenheit:", fahrenheit)

valid2 = [c for c in readings if -50 <= c <= 50]
fahrenheit2 = [c * 9 / 5 + 32 for c in valid2]
print("List Comprehension:", valid2)
print("Fahrenheit:", fahrenheit2)

valid3 = list(filter(lambda c: -50 <= c <= 50, readings))
fahrenheit3 = list(map(lambda c: c * 9 / 5 + 32, valid3))
print("Using Filter:", valid3)
print("Using Map:", fahrenheit3)

alarms = [minute for minute, temp in enumerate(readings, start=1) if temp < 2 or temp > 8]
print("Alarm Minutes:", alarms)
temp_dict = {i + 1: temp for i, temp in enumerate(readings) if -50 <= temp <= 50}
print("Dictionary:", temp_dict)
print("Set:", {c for c in valid})
gen = (c for c in readings if -50 <= c <= 50)
print("Generator:", list(gen))
