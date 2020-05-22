import numpy
N,M=list(map(int,input().split()))
el=[]
for i in range(N):
    n=list(map(int,input().split()))
    el.append(n)
my_array=numpy.array(el)
print(numpy.transpose(my_array))
print(my_array.flatten())