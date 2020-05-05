n = int(input())

for i in range(n):
    s = input()
    n1 = len(s)

    if n1 > 10:
        s1 = s[0] + str(n1-2) + s[-1]
        print(s1)
    else:
        print(s)