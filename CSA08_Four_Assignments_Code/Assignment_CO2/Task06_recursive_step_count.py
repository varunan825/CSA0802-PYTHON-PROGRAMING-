def ways(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ways(n - 1) + ways(n - 2)

n = int(input("Enter number of steps: "))
print("Number of ways:", ways(n))
