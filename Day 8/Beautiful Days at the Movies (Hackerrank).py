def rev_diff(n1):
    a2 = int(str(n2)[::-1])

    return abs(n1-a2)


f_line = input()
f_arr = [int(y) for y in f_line.split()]

i = f_arr[0]
j = f_arr[1]
k = f_arr[2]
b_days_count = 0

for x in range(i,j):
    ans = rev_diff(x)
    if ans%k == 0:
        b_days_count +=1
print(b_days_count)



