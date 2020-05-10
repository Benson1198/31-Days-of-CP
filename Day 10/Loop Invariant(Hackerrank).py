n = int(input())
a = input()
arr = [int(y) for y in a.split()]
arr.sort()
for i in range(n):
    print(arr[i], end=' ')