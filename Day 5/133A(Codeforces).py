s1 = 'HQ9'
s = input()

count = 0
for i in range(len(s)):
    if s[i] in s1:
        count += 1
    else:
        pass
if count:
    print('YES')
else:
    print('NO')