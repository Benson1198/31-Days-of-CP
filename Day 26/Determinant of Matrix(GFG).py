def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def determinant_fast(A):
    
    n = len(A)
    AM = copy_matrix(A)
 

    for fd in range(n): 
        for i in range(fd+1,n):
            if AM[fd][fd] == 0: 
                AM[fd][fd] == 1.0e-18

            crScaler = AM[i][fd] / AM[fd][fd] 

            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
     

    product = 1.0
    for i in range(n):

        product *= AM[i][i] 
 
    return product