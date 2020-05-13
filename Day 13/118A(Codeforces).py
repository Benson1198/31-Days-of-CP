s = input()

vowels = 'aeiouyAEIOUY'

lst = list(s)
new_lst = []

for i in range(len(lst)):
    if lst[i] in vowels:
        pass
    else:
        new_lst.append('.')
        new_lst.append(lst[i].lower())

s_new = ''.join(str(j) for j in new_lst)

print(s_new)