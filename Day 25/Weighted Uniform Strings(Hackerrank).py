#!/bin/python3

import os
import sys
from collections import Counter 

#
# Complete the weightedUniformStrings function below.
#
def weightedUniformStrings(s, queries):
    a = 'abcdefghijklmnopqrstuvwxyz'
    alpha = list(a)

    s_lst = list(s)
    set_lst = list(set(s))

    U = [0]
    res = []

    coun = Counter(s_lst)

    for i in set_lst:
        x = coun[i]
        weight = alpha.index(i) + 1

        for j in range(1,x+1):
            prod = j*weight
            U.append(prod)
    for k in queries:
        if k not in U:
            res.append('No')
        else:
            res.append('Yes')
            
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
