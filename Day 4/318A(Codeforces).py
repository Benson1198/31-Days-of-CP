f_line = input()
f_arr = [int(y) for y in f_line.split()]

n = f_arr[0]
k = f_arr[1]

even_arr = []
odd_arr = []

for i in range(1,k*2):
    if i%2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)

final_arr = odd_arr + even_arr

print(final_arr[k-1])