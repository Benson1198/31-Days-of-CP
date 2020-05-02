# https://codeforces.com/problemset/problem/271/A

n = int(input())
i = n+1
while i > n:
    st = str(i)
    if len(set(st)) == 4:
        print(i)
        break
    i += 1
