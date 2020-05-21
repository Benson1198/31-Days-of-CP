# A = array
# N = length of array
# K = group size

def reverseInGroups(A,N,K):
    temp_arr = []
    if N%K != 0:
        r = N%K
        for i in range(K-1,N,K):
            for j in range(i,i-K,-1):
                temp_arr.append(A[j])
        for i in range(-1,-r-1,-1):
            temp_arr.append(A[i])
    else:
        for i in range(K-1,N,K):
            for j in range(i,i-K,-1):
                temp_arr.append(A[j])
    return temp_arr