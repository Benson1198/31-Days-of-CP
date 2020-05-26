import numpy
x=list(map(float,input().split()))
y=float(input())
arr=numpy.array(x)
print(numpy.polyval(arr,y))