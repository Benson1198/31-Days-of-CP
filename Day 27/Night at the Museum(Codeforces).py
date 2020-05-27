def solve(stri):
    stri = 'a' + stri
    totalMoves = 0

    for i in range(1, len(stri)):
        prevChar = stri[i-1]
        curChar = stri[i]

        forwardMove = abs(ord(prevChar) - ord(curChar))
        backwardMove = 26 - forwardMove

        totalMoves += min(forwardMove, backwardMove)

    return totalMoves



s = input()
print(solve(s))