def search(n1, m1, mat, x):
    i=0
    j=m1-1
    while i<n1 and j>=0:
        if mat[i][j]==x:
            return 1
        elif mat[i][j] > x:
            j=j-1
        else:
            i=i+1
    return 0 



# for i in range(n1):
#         last_ele = mat[i][m1-1]
            
#         if x == last_ele:
#             return 1
#         elif x > last_ele:
#             continue
#         else:
#             for j in range(m1):
#                 if mat[i][j] == x:
#                     return 1
#                 else:
#                     continue
#             return 0
#     return 0