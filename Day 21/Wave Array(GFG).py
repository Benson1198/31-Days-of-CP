def convertToWave(A,N):
    for i in range(0,N,2):
        a = A.pop()
        A.insert(i,a)
        
    return A