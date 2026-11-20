import time

parts = ["Python"] * 10000

start = time.perf_counter()
result = ""
for part in parts:
    result = result + part
print("Using + :", time.perf_counter() - start)

start = time.perf_counter()
result = ""
for part in parts:
    result += part
print("Using += :", time.perf_counter() - start)

start = time.perf_counter()
result = "".join(parts)
print("Using join():", time.perf_counter() - start)
