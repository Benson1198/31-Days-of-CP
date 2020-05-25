#!/bin/python3

import os
import sys

def happyLadybugs(b):
    l=list(b)
    s=set(l)
    for i in s:
        if i.isalpha():
            if l.count(i)==1:
                return "NO"
    for i in range(len(l)-1):
        if l[i-1]==l[i] or l[i+1]==l[i]:
            continue
        elif l.count("_")==0:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
