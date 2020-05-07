def growth(value,n):
    for i in range(1,n+1):
        if i%2==0:
            value+=1
        else:
            value *= 2

    return value

    
t = int(input())
for _ in range(t):
    n = int(input())
    ans = growth(1,n)
    print(ans)