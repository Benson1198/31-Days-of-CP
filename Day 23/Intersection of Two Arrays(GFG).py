def printIntersection(a, b, n, m):
    set_lst_a = list(set(a))
    set_lst_b = list(set(b))
    
    intersection = []
    
    for i in set_lst_a:
        if i in set_lst_b:
            intersection.append(i)
            
    intersection.sort()
    
    s = ' '.join(str(y) for y in intersection)
    
    if len(intersection) == 0:
        return -1
    else:
        return