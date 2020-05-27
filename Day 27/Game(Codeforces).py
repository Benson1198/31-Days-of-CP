def solve(n1,n2):
    if(n1>n2):
        return "First"
    else:
        return "Second"


n1,n2,k1,k2 = [int(y) for y in input().split()]
print(solve(n1,n2,k1,k2))