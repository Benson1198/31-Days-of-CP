def solve(a, b, c):

    l = len(a)
    for i in range(0, l):

        if a[i] != c[i] and b[i] != c[i]:
                return "NO"

    return "YES"

    n = int(input())

    answers = []
    for i in range(0,n):
        a = input()
        b = input()
        c = input()
        answers.append(solve(a, b, c))

    for answer in answers:
        print(answer)