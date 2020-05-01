# https://codeforces.com/problemset/problem/69/A

n = int(input())
x_sum = 0
y_sum = 0
z_sum = 0

for _ in range(n):
    a = input()
    arr = [int(y) for y in a.split()]
    x_sum += arr[0]
    y_sum += arr[1]
    z_sum += arr[2]

if (x_sum,y_sum,z_sum) == (0,0,0):
    print("YES")
else:
    print("NO")
