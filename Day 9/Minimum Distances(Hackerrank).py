#!/bin/python3

import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

def minimumDistances(a):
    min_dist = -1
    if len(set(a)) == 1 and len(a) > 1:
        return 1
    for j in range(len(a) - 1, -1, -1):
        dist = j - a.index(a[j])
        if 0 < dist < min_dist or min_dist < 0 < dist :
            min_dist = dist
    
    return min_dist

print(minimumDistances(A))