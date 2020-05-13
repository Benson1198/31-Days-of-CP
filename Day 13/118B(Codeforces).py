def symm_print(n):
    lst = []
    rev_lst = []
    for i in range(n+1):
        lst.append(i)
    for j in range(n-1,-1,-1):
        rev_lst.append(j)
    sum_lst = lst + rev_lst
    
    s_new = ' '.join(str(j) for j in sum_lst)
    
    return s_new


n = int(input())

for i in range(n+1):
    spaces = ' '*2*(n-i)
    print(spaces+symm_print(i))
for i in range(n-1,-1,-1):
    spaces = ' '*2*(n-i)
    print(spaces+symm_print(i))