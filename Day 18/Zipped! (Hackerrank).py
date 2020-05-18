n,x=list(map(float,input().split()))
marks=[]
for i in range(int(x)):
    marks.append(list(map(float,input().split())))
res=(list(zip(*(i for i in marks))))
for i in range(int(n)):
    print((sum(res[i])/x))