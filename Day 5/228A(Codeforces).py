f_line = input()
f_arr = [y for y in f_line.split()]

dict_f = {}

for i in range(len(f_arr)):
    dict_f[f_arr[i]] = f_arr.count(f_arr[i])

lst = list(dict_f.values())

sum_lst = 0

for j in range(len(lst)):
    sum_lst += lst[j] - 1

print(sum_lst)