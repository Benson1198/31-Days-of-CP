n = int(input())
arr = [int(y) for y in input().split()]
max_num = max(arr)
min_num = min(arr)

max_count = arr.count(max_num)
min_count = arr.count(min_num)


diff = abs(max_num-min_num)

if max_num == min_num:
    ans = 1
else:
    ans = max_count*min_count

print(str(diff) + ' ' + str(ans))