def sumMatrix(n1, m1, n2, m2, arr1, arr2):
    sum_mat = [[0]*m1]*n1
    sum_arr = []
    
    if (n1==n2) and (m1==m2):
        for i in range(n1):
            for j in range(m1):
                sum_mat[i][j] = arr1[i][j] + arr2[i][j]
                sum_arr.append(sum_mat[i][j])
        for a in range(len(sum_arr)):
            print(sum_arr[a], end=' ')
    else:
        print('-1',end=' ')