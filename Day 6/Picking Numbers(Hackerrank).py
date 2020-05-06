#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    arr = a
    arr.sort()
    set_arr = list(set(a))
    set_arr.sort()
    max_len = 0
    for i in range(len(set_arr)):
        n = arr.count(set_arr[i]) + arr.count(set_arr[i] + 1)
        if n > max_len:
            max_len = n
    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()