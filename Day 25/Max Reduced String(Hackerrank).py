#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    s=list(s)
    k=s
    c=0
    while True:
        c=0
        s=k
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                del s[i+1]
                del s[i]
                c=1
                break
        if c==0:
            break
    return "Empty String" if len(k)==0 else ''.join(list(k))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
