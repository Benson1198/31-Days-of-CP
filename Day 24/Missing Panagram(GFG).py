def missingPanagram(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_lst = list(alpha)
    inp_lst = [y.lower() for y in list(s)]
    miss_lst = []
    
    for i in alpha_lst:
        if i not in inp_lst:
            miss_lst.append(i)
            
    miss_lst.sort()
    miss_s = ''.join(miss_lst)
    if len(miss_lst) == 0:
        return -1
    else:return miss_s