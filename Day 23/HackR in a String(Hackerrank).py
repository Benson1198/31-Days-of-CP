#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    l = list('hackerrank')
    n = len(s)
    for i in range(n-1, -1, -1):
        if l == []:
            return 'YES'
        if s[i] == l[-1]:
            l.pop()
    if l == []:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
