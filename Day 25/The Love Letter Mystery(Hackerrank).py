#!/bin/python3

import math
import os
import random
import re
import sys

def theLoveLetterMystery(s):
    s1=s[0:int(len(s)/2)]
    s=s[::-1]
    s2=s[0:int(len(s)/2)]
    d=0
    for i in range(len(s1)):
        d+=abs((ord(s1[i])-ord(s2[i])))
    return d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
