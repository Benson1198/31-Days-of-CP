def subarrayZero(arr):
    a = arr.index(0)
    b = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(i+1,len(arr)):
                if j == (len(arr)-1):
                    b = j
                    break
                elif arr[j] != 0:
                    b = j-1
                    break
            break
    if b+1 == 1:
        return [a+1,a+1]
    else:
        return [a+1,b+1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr_zero = [0]*n
    if n == 1:
        print(1)
    else:
        for i in range(1,n+1):
            lr = subarrayZero(arr_zero)
            l = lr[0]
            print(l)
            r = lr[1]
            print(r)
            check = r-l+1
            if check%2 != 0:
                op = int((l+r)/2)
                arr_zero[op-1] = i
                print(arr_zero)
            else:
                op = int((l+r-1)/2)
                arr_zero[op-1] = i
                print(arr_zero)
        print(' '.join(str(a) for a in arr_zero))
