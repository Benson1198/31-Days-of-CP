from math import gcd

def getSmallestDivNum(n):

    a = [int(y) for y in range(1,n+1)]   
    lcm = a[0]
    for i in a[1:]:
      lcm = int(lcm*i/gcd(lcm, i))
    return int(lcm)