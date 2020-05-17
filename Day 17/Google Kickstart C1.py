t = int(input())
for _ in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = [str(y) for y in input().split()]

    k_lst = [str(y) for y in range(k,0,-1)]
    k_str = ''.join(k_lst)
    arr_str = ''.join(arr)

    count = arr_str.count(k_str)
    print(count)