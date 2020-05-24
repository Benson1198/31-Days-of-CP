def findMissing(arr, size): 
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
    
    return len(arr) + 1