try:
    T=int(input())
    for t in range(T):
        n = int(input())
        lis = list(map(int,input().split()))
        pos = int(input())
        temp = lis[pos-1]
        lis.sort()
        print(lis.index(temp)+1)
except:
    pass