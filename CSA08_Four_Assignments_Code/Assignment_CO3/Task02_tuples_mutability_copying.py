import copy

rows, cols = 3, 4
bad = [[0] * cols] * rows
bad[0][1] = 7
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7
print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])

stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}
print(stops[(13.0418, 80.2341)])
for (latitude, longitude), name in stops.items():
    print(name, latitude, longitude)

a = [10, 20, 30]
b = a
b[0] = 100
print("Aliasing:", a)
c = copy.copy(a)
c[1] = 200
print("Original:", a)
print("Shallow Copy:", c)
d = copy.deepcopy(a)
d[2] = 300
print("Deep Copy:", d)

t = ([1, 2, 3], 10)
t[0].append(4)
print("Tuple with list:", t)
