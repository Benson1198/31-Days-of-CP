def sumUnderModulo(a,b):

    M = 1000000007
    
    am = a % M
    bm = b % M
    
    sum = am + bm
    
    while sum > M:
        sum = sum % M
    
    return sum