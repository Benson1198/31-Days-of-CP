def isKBitSet(n, k): 
    if n & (1 << (k - 1)): 
        print( "Set") 
    else: 
        print("Not Set") 