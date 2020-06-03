# https://codeforces.com/problemset/problem/266/B

def swapper(arr,a):
    temp = arr[a]
    arr[a] = arr[a+1]
    arr[a+1] = temp

f_line = input()
f_arr = [int(y) for y in f_line.split()]
n = f_arr[0]
t = f_arr[1]

s_line = input()
arr = list(s_line)


for x in range(t):
    i = 0
    for y in range(n-1):
        if arr[i] = 'B' and arr[i+1] = 'G':
            swapper(arr,i)
            i += 2
        else:
            i += 1

answer = ''.join(arr)

print(answer)        
