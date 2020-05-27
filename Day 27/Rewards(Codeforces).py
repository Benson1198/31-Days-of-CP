def solve(n, cups, medals):

    cupsSum = sum(cups)
    cup_shelves_needed = cupsSum / 5

    if cupsSum % 5 != 0:
        cup_shelves_needed += 1

    medalsSum = sum(medals)
    medal_shelves_needed = medalsSum / 10

    if medalsSum % 10 != 0:
        medal_shelves_needed += 1

    return "YES" if (cup_shelves_needed + medal_shelves_needed) <= n else "NO"

cups = [int(y) for y in input().split()]
medals = [int(y) for y in input().split()]
n = int(input())
print(solve(n,cups,medals))