n = int(input())
f_line = input()
f_arr = [int(y) for y in f_line.split()]

n1 = n+1
sum_arr = sum(f_arr)

fing_arr = [1,2,3,4,5]

for i in fing_arr:
    copy_arr = fing_arr.copy()
    temp_sum = sum_arr + i
    if temp_sum % n1 == 1:
        copy_arr.remove(i)
    
print(copy_arr[0])
