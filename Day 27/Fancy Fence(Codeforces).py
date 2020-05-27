def solve(angle):

    if 360 % (180 - angle) != 0:
        return "NO"
    else:
        return "YES"

cases = int(input())
results = list()
for case in range(0,cases):
    angle = int(input())
    results.append(angle)
for result in results:
    print(solve(result))