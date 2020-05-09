n = int(input())
a = input()
arr = [int(y) for y in a.split()]
max_count = 0
set_lst = list(set(arr))
for i in range(len(set_lst)):
    if arr.count(set_lst[i]) > max_count:
        max_count = arr.count(set_lst[i])
ans = len(arr) - max_count
print(ans)