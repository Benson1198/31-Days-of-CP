def Search(arr,n,k):
    try:
        ind = arr.index(k)
        return ind
    except:
        return -1