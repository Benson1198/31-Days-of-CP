#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    a =arr.pop()
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>a:
            arr.append(arr[i])
            print (' '.join(map(str, sorted(arr))))
            arr.pop()
        elif arr[i]<a:
            arr.append(a)
            print (' '.join(map(str, sorted(arr))))
            if sorted(arr):
                break
    if a == 1:
        arr.append(a)
        print (' '.join(map(str, sorted(arr))))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
