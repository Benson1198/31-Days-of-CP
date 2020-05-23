#!/bin/python3

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    g=set([x for x in s])
    f=0
    for  h in g:
        if s.count(h)%2!=0:
            f+=1
            if f>1:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
