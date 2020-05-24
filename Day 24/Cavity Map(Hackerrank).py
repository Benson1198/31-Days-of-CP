#!/bin/python3

import math
import os
import random
import re
import sys


def adjacent_checker(arr,i,j):
    a = (arr[i][j] > arr[i-1][j]) and (arr[i][j] > arr[i+1][j]) and (arr[i][j] > arr[i][j+1]) and (arr[i][j] > arr[i][j-1])

    if a:
        return True
    else:
        return False


def cavityMap(grid):
    n = len(grid)
    if n <= 2:
        return grid
    else:
        grid_arr = []
        ret_grid = []

        for a in range(n):
            arr = [int(y) for y in grid[a].split()]
            grid_arr.append(arr)
        
        for i in range(1,n-1):
            for j in range(1,n-1):
                if adjacent_checker(grid_arr,i,j):
                    grid_arr[i][j] = 'X'
        
        for b in range(n):
            ab = ''.join(str(y) for y in grid_arr[b])
            ret_grid.append(ab)
        
        return ret_grid
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
