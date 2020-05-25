
try:
    T=int(input())
    for t in range(T):
        g=int(input())
        for _ in range(g):
            i,n,q=map(int,input().split())
            h=0
            t=0
            if(n%2!=0):
                if(i==1):
                    h=n//2
                    t=n-h
                else:
                    t=n//2
                    h=n-t
            else:
                h=n//2
                t=h
            if(q==1):
                print(h)
            else:
                print(t)
except:
    pass