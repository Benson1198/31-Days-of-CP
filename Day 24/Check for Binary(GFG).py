def isBinary(str):
    lst = list(str)
    for i in lst:
        if int(i) == 0 or int(i) ==1:
            continue
        else:
            return False
    return True
