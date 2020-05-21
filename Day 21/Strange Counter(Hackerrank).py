#!/bin/python3

import math
import os
import random
import re
import sys

def strangeCounter(t):
    end=i=0
    while t>end:
        end=end+3*(2**i)
        i+=1
    return (end-t+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
