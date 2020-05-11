from collections import Counter
number_of_shoe=int(input())
size_of_shoe=list(map(int,input().split()))
number_of_customer=int(input())
k=Counter(size_of_shoe).items()
a=[]
s=0
for i in k:
    a.append(list(i))

for i in range(number_of_customer):
    d=tuple(input().split())
    for x in range(len(k)):
        if a[x][0]==int(d[0]) and a[x][1]!=0:
            s=s+int(d[1])
            a[x][1]=a[x][1]-1
            

print(s)