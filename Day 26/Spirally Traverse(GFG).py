def spirallyTraverse(m, n, a) :
    k = 0
    l = 0
    
    out_arr = []
    
    while k< m and l < n:
        for i in range(l,n):
            out_arr.append(a[k][i])
        k += 1
        
        for i in range(k,m):
            out_arr.append(a[i][n-1])
        n -= 1
        
        if k<m:
            for i in range(n-1,l-1,-1):
                out_arr.append(a[m-1][i])
            m -= 1
        
        if l< n:
            for i in range(m-1,k-1,-1):
                out_arr.append(a[i][l])
            l += 1
            
    for j in out_arr:
        print(j,end=' ')