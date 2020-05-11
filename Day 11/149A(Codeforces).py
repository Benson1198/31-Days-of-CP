k = int(input())
arr = [int(y) for y in input().split()]
arr.sort()

month_count = 0

if sum(arr) < k:
    print(-1)

else:
    for i in range(12):
        if k == 0:
            break
        else:
            k -= arr[::-1][i]
            month_count += 1
            if k <= 0:
                break


    print(month_count)