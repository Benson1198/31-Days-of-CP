import numpy

n,m=map(int,input().split())
x=numpy.array(numpy.eye(n,m,dtype=float))
print('[',end='')
for i in range(len(x)):
        if i!=0:
                print(' ',end='')
        print('[',end='')
        for j in range(len(x[i])):
                if j==0:
                        print(' ',end='')
                else:
                        print('  ',end='')  
                print(('{:.1f}'.format(x[i][j]))[:2],end='')
if i==len(x)-1:
    print(']',end='')
else:
    print(']')