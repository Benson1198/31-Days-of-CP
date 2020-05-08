t = int(input())
for _ in range(t):
    f_line = input()
    f_arr = [int(y) for y in f_line.split()]
    s_line = input()
    s_arr = [int(y) for y in s_line.split()]
    n = f_arr[0]
    k = f_arr[1]
    count_early = 0

    for i in range(n):
        if s_arr[i] <= 0:
            count_early += 1
    if count_early >= k:
        print('NO')
    else:
        print('YES')