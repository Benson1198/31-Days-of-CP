# https://codeforces.com/problemset/problem/227/B

n = int(input())
f_line = input()
f_arr = [int(y) for y in f_line.split()]
f_arr_rev = f_arr.copy()[::-1]

m = int(input())
q_line = input()
q_arr = [int(y) for y in q_line.split()]

vasya_count = 0
petya_count = 0

for i in range(m):
    vasya_count += (f_arr.index(q_arr[i])) +1
    petya_count += (f_arr_rev.index(q_arr[i])) +1

print(str(vasya_count) + ' ' + str(petya_count))