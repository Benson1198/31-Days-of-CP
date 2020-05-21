def rotateArr(A,D,N):
    D=D%N
    A[:]= A[D:] + A[:D]
    return (A)
