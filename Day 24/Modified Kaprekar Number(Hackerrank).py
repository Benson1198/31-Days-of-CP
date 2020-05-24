#!/bin/python3

import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    if(p>-1):
        st=""
        for i in range(p,q+1):
            sq=i**2
            l2=len(str(sq))
            l1=len(str(sq))//2
            sq1=str(sq)
            if(l1==0 and sq!=0):
                j=int(sq1[0])
                if(j==i):
                    st=st+""+str(i)+" "
            if(l2>1):
                k=int(sq1[:l1])+int(sq1[l1:])
                if(k==i):
                    st=st+""+str(i)+" "
        if(len(st)==0):
            print("INVALID RANGE")
        else:
            print(st)

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
