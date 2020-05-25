t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    c=list(map(int,input().split()))
    m=[]
    a=[]
    j=[i for i in range(1,n+1)]
    for i in c:
        if i in j:
            j.remove(i)
    for i in range(len(j)):
        if i%2!=0:
            m.append(j[i])
        else:
            a.append(j[i])
    a.sort()
    m.sort()
    if a==[]:
        print()
    else:
        for i in a:
            print(i,end=' ')
    print()        
    if m==[]:
        print()
    else:
        for i in m:
            print(i,end=' ')
    print()