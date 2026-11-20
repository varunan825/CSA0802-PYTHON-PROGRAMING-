import random

readings = [random.randint(0, 50) for _ in range(365)]
weekly_totals = [sum(readings[i:i + 7]) for i in range(0, len(readings), 7)]
print("Weekly Totals:", weekly_totals)
print("Maximum Rainfall:", max(readings))
print("Minimum Rainfall:", min(readings))

moving_average = [
    sum(readings[i:i + 7]) / 7
    for i in range(len(readings) - 6)
]
print("7-Day Moving Average:", moving_average)
dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]
print("Dry Days:", dry_days)
print("Readings[7:14]:", readings[7:14])
print("Last 7 Days:", readings[-7:])
print("Every 7th Reading:", readings[::7])
