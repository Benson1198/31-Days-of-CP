from itertools import permutations
n = input().split()

s = n[0]
k = int(n[1])

lst = list(permutations(s,k))
lst.sort()

for i in lst:
    print(''.join(i))