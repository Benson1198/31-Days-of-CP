n = int(input())
data = []
for _ in range(n):
    item = input()
    data.append((len(item), item))
for s in sorted(data):
    print(s[1])