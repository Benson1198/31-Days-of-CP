t = int(input())
for _ in range(t):
    f_line = input()
    f_arr = [int(y) for y in f_line.split()]
    n = f_arr[0]
    m = f_arr[1]
    s = f_arr[2]

    if((s+m-1)%n==0):
        print(n)
    else:
        print((s+m-1)%n)