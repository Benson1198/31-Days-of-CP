# https://codeforces.com/problemset/problem/266/B

def swapper(arr,i):
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp

f_line = input()
f_arr = [int(y) for y in f_line.split()]
n = f_arr[0]
t = f_arr[1]

