def floorSqrt(x): 
    
    arr = []
    for i in range(int(x/2)):
        arr.append(int(i*i))
    for j in range(len(arr)):
        if arr[j] == x:
            return j
        elif arr[j] > x:
            return j-1