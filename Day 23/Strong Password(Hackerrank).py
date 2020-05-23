#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    password=list(password)
    f=password.copy()
    password=set(password)
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case =set ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    c=0
    if len(password & numbers)!= 0:
        c+=1
    if len(password & lower_case)!= 0:
        c+=1
    if len(password & upper_case)!=0:
        c+=1
    if len(password & special_characters)!=0:
        c+=1
    if(len(f)+4-c)>=6:
        return 4-c
    else:
        return 6-len(f)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
