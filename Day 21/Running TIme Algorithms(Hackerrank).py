#!/bin/python3

import math
import os
import random
import re
import sys


def runningTime(arr):
    count = 0
    for index in range(len(arr)):
        for j in range(index,len(arr)):
            if arr[j] < arr[index]:
                count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
