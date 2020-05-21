def majorityWins(arr, n,  x,y):
    x_count = arr.count(x)
    y_count = arr.count(y)
    
    if x_count > y_count:
        return x
    elif x_count < y_count:
        return y
    else:
        return min(x,y)
