def cutTheSticks(arr):
    out = []
    while sum(arr) > 0:
        tc = 0
        minval = max(arr)
        for i in range(len(arr)):
            if arr[i] < minval and arr[i] != 0:
                minval = arr[i]
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i] -= minval
                tc += 1
        out.append(tc)
    return out


n = int(input())
a = input()
len_arr = [int(y) for y in a.split()]

num_arr = cutTheSticks(len_arr)

for i in range(len(num_arr)):
    print(num_arr[i])