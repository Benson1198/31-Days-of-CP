def rotateby90(a, n):
    for i in range(n):
        b = n - 1
        for j in range(n//2):
            a[i][j], a[i][b] = a[i][b], a[i][j]
            b -= 1
            
    for i in range(n):
        for j in range(i+1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
