def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def irr_fraction(num,dem):
    g = gcd(num,dem)
    while(g>1):
        num/=g
        dem/=g
        g = gcd(num,dem)

    print(str(int(num))+"/"+str(int(dem)))


def solve(y,w):

    avlbl = min(6,6-max(y,w)+1)
    irr_fraction(avlbl,6)



y,w = [int(y) for y in input().split()]
solve(y,w)