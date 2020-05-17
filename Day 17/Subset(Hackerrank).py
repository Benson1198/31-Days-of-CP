n=int(input())
for i in range(n):
    len_set1=int(input())
    set1=set(map(int,input().split()))
    len_set2=int(input())
    set2=set(map(int,input().split()))
    if len(set2.intersection(set1))==len(set1):
        print("True")
    else:
        print("False")