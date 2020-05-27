n,k = input().split()
k = int(k)
n = int(n)

for y in range(k):
    if int(str(n)[-1]) != 0:
        n -= 1
    else:
        n = int(n/10)

print(n) 



