#!/bin/python3

import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr.sort()
    min_diff = 20000001

    pair_arr = []
    res_arr = []

    for i in range(len(arr)-1):
        abs_diff = abs(arr[i] - arr[i+1])
        if abs_diff < min_diff:
            pair_arr.clear()
            min_diff = abs_diff
            pair_arr.append([arr[i],arr[i+1]])
        elif abs_diff == min_diff:
             pair_arr.append([arr[i],arr[i+1]])
        else:
            pass
    
    for i in range(len(pair_arr)):
        res_arr.append(pair_arr[i][0])
        res_arr.append(pair_arr[i][1])
    
    res_arr.sort()

    return res_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
