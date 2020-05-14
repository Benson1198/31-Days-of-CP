s = list(input())

word = 'hello'
count = 0

for i in range(len(s)):
    if count == 5:
        break
    elif s[i] == word[count]:
        count += 1
if count == 5:
    print('YES')
elif count < 5:
    print('NO')