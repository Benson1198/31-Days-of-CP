free = "OO"
book = "++"
aisle = "|"
bus = []

def solve(n):

    ans = "NO"
    for i in range(0,n):
        sides = bus[i].split(aisle)

        if sides[0] == free:
            bus[i] = book + aisle + sides[1]
            ans = "YES"
            break
        elif sides[1] == free:
            bus[i] = sides[0] + aisle + book
            ans = "YES"
            break

    return ans

n = int(input())
for i in range(0,n):
    bus.append(input())

ans = solve(n)

print(ans)

if ans == "YES":
    for i in range(0,n):
        print(bus[i])