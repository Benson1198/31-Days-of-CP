#!/bin/python3
import math
import os
import random
import re
import sys

def acmTeam(topic):
    res_max = 0
    res_ways = 0
    for i in range(len(topic)-1):
        for j in range(i+1, len(topic)):
            a, b = int(topic[i], 2), int(topic[j], 2)
            num_topics = bin(a|b).count('1')
            if num_topics > res_max:
                res_max = num_topics
                res_ways = 1
            elif num_topics == res_max:
                res_ways += 1
    return res_max, res_ways



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
