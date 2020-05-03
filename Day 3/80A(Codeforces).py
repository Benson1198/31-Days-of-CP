def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def next_prime(number):
    next_number = number + 1
    while not isprime(next_number):
        next_number += 1
    return next_number

f_line = input()
f_arr = [int(y) for y in f_line.split()]

lower = f_arr[0]
next_n = f_arr[1] 

temp = next_prime(lower)

if temp == next_n:
    print('YES')

else:
    print('NO')