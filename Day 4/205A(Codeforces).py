n = int(input())

f_line = input()
f_arr = [int(y) for y in f_line.split()]

min_ele = min(f_arr)

if f_arr.count(min_ele) > 1:
    print('Still Rozdil')
else:
    print(f_arr.index(min_ele) +1)