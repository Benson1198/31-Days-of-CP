#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(inpu):
    
    count=0
    i=len(inpu)
    for x in range(i,0,-1):
        if inpu[x-1]%2!=0:
            inpu[x-1]=inpu[x-1]+1
            inpu[x-2]=inpu[x-2]+1
            count=count+2


    if sum(inpu)%2==0:
        return(count)

    else:
        return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
