def getMaxOccurringChar(s):
    lst = list(s)
    lst.sort()
    set_lst = list(set(s))

    set_lst.sort()

    max_count = [0,'a']
    
    for i in set_lst:
        c = lst.count(i)
        if c > max_count[0]:
            max_count = [c,i]
    
    return max_count[1]