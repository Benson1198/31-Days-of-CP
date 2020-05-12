def smallest_divisor(n):
    for i in range(2,n+1):
        if n%i == 0:
            return i
            break

def func_n(n):
    return smallest_divisor(n) + n


t = int(input())
for _ in range(t):
    s = input().split()
    n = int(s[0])
    k = int(s[1])

    for i in range(k):
        n = func_n(n)
    print(n)

