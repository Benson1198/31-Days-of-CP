n = int(input())

f_line = input()
f_arr = [int(y) for y in f_line.split()]

min_diff = 1000

temp = 0

for i in range(len(f_arr)-1):
    if abs(f_arr[i] - f_arr[i+1]) < min_diff:
        temp = i+1
        min_diff = abs(f_arr[i] - f_arr[i+1])

if abs(f_arr[0]-f_arr[-1]) < min_diff:
    print(str(len(f_arr)) + ' ' + '1')
else:
    print(str(temp) + ' ' + str(temp+1))
        