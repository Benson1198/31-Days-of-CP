l,b = [int(y) for y in input().split()]
years = 0

while l<=b:
    l *= 3
    b *= 2
    years += 1

print(years)