import numpy as np
N, M=map(int, input().rstrip().split())
lst1=[]
lst2=[]
for _ in range(N):
    lst=list(map(int, input().rstrip().split()))
    lst1.append(lst)
a=np.array(lst1)
for _ in range(N):
    lst=list(map(int, input().rstrip().split()))
    lst2.append(lst)
b=np.array(lst2)
print(np.add(a,b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))