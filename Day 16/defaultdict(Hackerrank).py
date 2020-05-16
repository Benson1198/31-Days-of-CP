from collections import defaultdict
d=defaultdict(list)
a,b=map(int,input().split())
for i in range(a):
    d[input()].append(i+1)
for j in range(b):
    temp=input()
    print(*d.get(temp,[-1]))