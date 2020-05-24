t=int(input()) 
for kk in range(t): 
    n,k=map(int,input(). split()) 
    a=[int(x) for x in input().split()]  
    a.sort()
    if k<=n//2: 
        b=sum(a[:k]) 
        c=sum(a[k:]) 
    else: 
        b=sum(a[:n-k]) 
        c=sum(a[n-k:]) 
    print (abs(b-c))