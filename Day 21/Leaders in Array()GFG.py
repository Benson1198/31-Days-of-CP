def leaders(A,N):
    temp_arr = [A[-1]]
    max_ele = A[-1]
    A.reverse()
    for i in range(1,N):
        if A[i] >= max_ele:
            max_ele = A[i]
            temp_arr.append(A[i])
    arr = reversed(temp_arr) 
    return arr
