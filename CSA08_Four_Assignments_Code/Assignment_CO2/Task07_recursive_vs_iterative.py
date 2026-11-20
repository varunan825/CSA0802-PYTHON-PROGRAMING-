import time

def recursive_ways(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return recursive_ways(n - 1) + recursive_ways(n - 2)

def iterative_ways(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

n = int(input("Enter number of steps: "))
start = time.perf_counter()
print("Recursive result:", recursive_ways(n))
print("Recursive time:", time.perf_counter() - start)
start = time.perf_counter()
print("Iterative result:", iterative_ways(n))
print("Iterative time:", time.perf_counter() - start)
