n = int(input())
count_1 = 0
for _ in range(n):
    a = input()
    arr = [int(y) for y in a.split()]
    if arr.count(1) >= 2:
        count_1 += 1
print(count_1)