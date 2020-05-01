# https://codeforces.com/problemset/problem/263/A

for i in range(5):
    a = input()
    arr = [y for y in a.split()]
    if '1' in arr:
        column = i
        row = arr.index('1')

min_swaps = abs(2-column) + abs(2-row)
print(min_swaps)
