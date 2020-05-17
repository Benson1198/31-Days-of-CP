#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    i,j=p,0
    count=0
    if(p==1):
        return s
    while(i>=m):
        j+=i
        i=i-d
        if(j<=s):
            count+=1
    if(count>0):
        while(j<s):
            j+=m
            if(j<=s):
                count+=1
    return count
    # Return the number of games you can buy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
