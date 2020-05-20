def digitsInFactorial(N):
    num = N
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial*i
    
    return int(math.log10(factorial) + 1)
    