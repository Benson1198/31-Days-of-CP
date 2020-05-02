https://codeforces.com/problemset/problem/59/A

s = input()
lst = list(s)

upper_s = 0
lower_s = 0

for i in range(len(lst)):
    if lst[i].isupper():
        upper_s += 1
    else:
        lower_s += 1

if upper_s < lower_s:
    print(s.lower())
elif lower_s < upper_s:
    print(s.upper())
else:
    print(s.lower())

