s = input()
lst = list(s)
upper_count = 1
for i in range(len(lst)):
    if lst[i].isupper():
        upper_count += 1
print(upper_count)