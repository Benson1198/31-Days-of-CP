t = int(input())
for _ in range(t):
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    if n ==1:
        print(0)
    if n == 2:
        print(m)
    if n > 2:
        print(2*m)