def solve(arr):

    arrSet = set(arr)
    isZeroElemPresent = False

    for a in arrSet:
        if a == 0:
            isZeroElemPresent = True
            break

    return len(arrSet) - (1 if isZeroElemPresent else 0)


n = int(input())
arr = [int(y) for y in input().split()]
print(solve(arr))