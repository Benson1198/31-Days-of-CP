#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    worst = scores[0]
    best = scores[0]
    b_count = 0
    w_count = 0

    for i in range(1, n):
        if scores[i] < worst:
            w_count += 1
            worst = scores[i]
        elif scores[i] > best:
            b_count += 1
            best = scores[i]
        else:
            pass
    ans = [b_count,w_count]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
