import numpy as np

x = input().split()
a1 = int(x[0])
a2 = int(x[1])
a3 =  int(x[2])
list_new1 = []
list_new2 = []


for i in range(0,a1):
    c = list(map(int,input().split()))
    list_new1.append(c)

for i in range(0,a2):
    c1 = list(map(int,input().split()))
    list_new2.append(c1)

array_1 = np.array(list_new1)
array_2 = np.array(list_new2)

print(np.concatenate((array_1,array_2)))