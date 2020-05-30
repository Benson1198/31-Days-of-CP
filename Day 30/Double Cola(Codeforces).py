def solve(n):

    map = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

    rate = 1
    while (5 * rate) <= n:
        n -= (5 * rate)
        rate *= 2
    return map[(n-1)/rate]

n = int(input())
print(solve(n))