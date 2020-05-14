t = int(input())
for _ in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a_arr = [int(y) for y in input().split()]
    b_arr = [int(y) for y in input().split()]
    a_arr.sort()
    b_arr.sort(reverse=True)

    for i in range(k):
        if a_arr[i] < b_arr[i]:
            a_arr[i] = b_arr[i]
    print(sum(a_arr))