from itertools import permutations

def permutation(S):
    perm = permutations(S)
    lst = []
    for i in perm:
        temp = list(i)
        lst.append(''.join(temp))
    ans = ' '.join(lst)    
    return ans 