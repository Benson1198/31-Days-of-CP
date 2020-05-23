n = int(input())
lst = input().split()
counts = dict()
for item in lst:
    counts[item] = counts.get(item,0)+1

for k,v in counts.items():
    if v ==1:
        print(k)