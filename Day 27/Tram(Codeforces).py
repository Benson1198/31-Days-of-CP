max_count = 0
passengers = 0
for _ in range(int(input())):
    a,b = [int(y) for y in input().split()]
    passengers -= a
    passengers += b

    if passengers > max_count:
        max_count = passengers
    else:
        continue
if max_count <= 0:
    print(0)
else:
    print(max_count)