#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    total=0
    if len(c)%k==0:
        for i in range(0,len(c),k):
            total+=1
            if c[i]==1:
                total+=2
    elif len(c)%k!=0:
        for i in range(0,len(c)):
            total+=1
            if c[i]==1:
                total+=2
    return (100-total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
