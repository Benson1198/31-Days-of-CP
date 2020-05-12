#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    i=len(s)
    while k>0:
        if k<=len(t)-len(s):
            if s=='':
                i=0
            s=s+t[i]
            i+=1
            k-=1    
        else:
            k-=1
            i-=1
            s=s[:i]        
    
    if(k==0 and s==t):
        return("Yes")
    else:
        return("No")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
