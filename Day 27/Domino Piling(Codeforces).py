def solve(m, n):
    tileArea = 2*1
    boardArea = m*n
    return boardArea / tileArea


m, n = [int(y) for y in input().split()]
ans = solve(m,n)
print(int(ans))