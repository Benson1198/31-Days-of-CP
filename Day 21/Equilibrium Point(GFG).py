def equilibriumPoint(A, N):
    n = N
    arr = A 
    leftsum = 0
    rightsum = 0
    for i in range(n): 
        leftsum = 0
        rightsum = 0
      
        for j in range(i): 
            leftsum += arr[j] 
          
        for j in range(i + 1, n): 
            rightsum += arr[j] 
          
        if leftsum == rightsum: 
            return i +1
      
    return -1