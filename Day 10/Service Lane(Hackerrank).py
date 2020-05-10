nt = input().split()

n = int(nt[0])

t = int(nt[1])

width = list(map(int, input().rstrip().split()))

cases = []

for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

for i in range(len(cases)):
    arr=[]
    for j in range(cases[i][0],cases[i][1]+1):
        arr.append(width[j])

    print(min(arr))