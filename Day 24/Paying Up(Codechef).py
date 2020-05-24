from itertools import combinations
for i in range(int(input())):
    n,m=[int(i) for i in input().split()]
    lst=[]
    for i in range(n):
        lst.append(int(input()))
    lst2=[]
    for i in range(1,n+1):
        lst2.append(list(combinations(lst,i)))
    nd=1
    for i in lst2:
        for j in i:
            if sum(j)==m:
                print('Yes')
                nd=0
                break
        if nd==0:
            break
    if nd==1:
        print('No')