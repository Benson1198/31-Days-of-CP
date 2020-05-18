a= set(map(int, input().split()))
n= int(input())
result= True
for i in range (0,n):
    b= set(map(int, input().split()))
    if not a.issuperset(b):
        result= False

print(result)