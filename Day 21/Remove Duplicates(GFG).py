def remove_duplicate(n, arr):
    temp_arr = [arr[0]]
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            temp_arr.append(arr[i])
    return temp_arr