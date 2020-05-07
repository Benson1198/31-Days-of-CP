n = int(input())
value = 0
for _ in range(n):
    a = input()
    if '+' in a:
        value += 1
    elif '-' in a:
        value -= 1
print(value)