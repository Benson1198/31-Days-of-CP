from math import sqrt
s = input().split()

a1 = int(s[0])
a2 = int(s[1])
a3 = int(s[2])

a = sqrt(a1*a3/a2)
b = sqrt(a1*a2/a3)
c = sqrt(a2*a3/a1)

ans = int(4*(a+b+c))
print(ans)