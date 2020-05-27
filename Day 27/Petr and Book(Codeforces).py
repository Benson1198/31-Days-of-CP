def solve(n, daily):

    i = 0
    while n - daily[i] > 0:

        n -= daily[i]
        i = (i+1) % 7

    return i+1

n = int(input())
arr = [int(y) for y in input().split()]

print(solve(n,arr))

