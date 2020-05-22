from bisect import *
def bin_search(arr, left, high, key):
    #Code here
    high-=1
    i = bisect(arr, key, left, high)
    if i == 0:
        return (-1)
    elif arr[i-1] == x:
        return (i-1)
    else:
        return (-1)