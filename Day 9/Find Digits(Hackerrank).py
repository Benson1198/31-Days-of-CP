t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(y) for y in list(str(n))]
    div_count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            pass
        else:
            if n%arr[i] == 0:
                div_count += 1
            else:
                pass
    print(div_count)
    