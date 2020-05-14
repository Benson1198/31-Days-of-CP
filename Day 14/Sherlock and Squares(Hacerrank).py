import math 
  
def squares(a, b):
    x = math.ceil(math.sqrt(a))
    y = int(math.sqrt(b))
    return len(range(x, y+1))

t = int(input())
for _ in range(t):
    n = input().split()
    l = int(n[0])
    r = int(n[1])
    print(squares(l,r))

