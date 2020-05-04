n = int(input())

f_line = input()
f_arr = [int(y) for y in f_line.split()]

sum_arr = sum(f_arr)

d = (sum_arr/n)
print(d)