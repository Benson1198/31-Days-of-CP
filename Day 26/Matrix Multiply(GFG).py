def multiplyMatrix(n1, m1, n2, m2, arr1, arr2):
    
    if m1==n2:
        for i in range(n1):
            for j in range(m2):
                sum_arr = 0
                for k in range(m1):
                    sum_arr += arr1[i][k] * arr2[k][j]
                print(sum_arr, end=' ')
                
    else:
        print('-1',end=' ')