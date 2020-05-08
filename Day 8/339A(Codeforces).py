f_line = input()
f_arr = [y for y in f_line.split('+')]
f_arr.sort()

print('+'.join(f_arr))