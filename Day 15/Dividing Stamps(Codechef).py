def sum1(n):
    sm=0
    for i in range(n+1):
        sm+=i
    return sm

n=int(input())
a=list(map(int,input().strip().split()))[:n]
sm=0
for i in range(len(a)):
    sm+=a[i]
if sum1(n)==sm:
    print("YES")
else:
    print("NO")