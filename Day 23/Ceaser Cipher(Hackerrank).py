#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    res = ""  
    for i in range(len(s)): 
        char = s[i] 
        if char.isalpha(): 
            if (char.isupper()): 
                res += chr((ord(char) + k-65) % 26 + 65) 
            else: 
                res += chr((ord(char) + k - 97) % 26 + 97) 
        else:
            res += char
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
