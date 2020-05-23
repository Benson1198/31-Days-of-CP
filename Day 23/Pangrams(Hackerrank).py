#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    lst1 = s.split(' ')
    s_without_space = ''.join(word.lower() for word in lst1)
    lst_s = list(s_without_space)

    set_s = set(lst_s)
    if len(set_s) == 26:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
