#!/bin/python3

import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    p = 1
    i = 0
    result = 0
    for i in range(n):
        cha = list(range(p, p+math.ceil(arr[i]/k)))
        pro = list(range(1, arr[i]+1))
        for c in cha:
            if (c in pro and math.ceil(c/k)==cha.index(c)+1):
                result += 1
        p = p+math.ceil(arr[i]/k)
        i += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
