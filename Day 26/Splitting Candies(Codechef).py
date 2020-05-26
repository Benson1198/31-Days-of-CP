for _ in range(int(input())):
    n,k=map(int,input().split())
    if k == 0:
        print (0,n)
        continue
    print (n//k, n%k)