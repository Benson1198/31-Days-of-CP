def solve(keyboards):

    keyboards.sort()

    stolen = 0

    for i in range(1, len(keyboards)):

        if keyboards[i] - keyboards[i-1] > 1:
            stolen += keyboards[i] - keyboards[i-1] - 1

    return stolen



n = int(input())
keyboards = [int(y) for y in input().split()]
print(solve(keyboards))