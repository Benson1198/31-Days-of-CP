n, m, a, b = [int(y) for y in input().split()]
res1 = 0
res2 = 0


p = n/m

res1 += p*b
if(n%m!=0):
    if((n-(m*p))*a < b):
        res1 += (n-(m*p))*a
    else:
        res1 += b

res2 = n*a
print(min(int(res1),int(res2)))