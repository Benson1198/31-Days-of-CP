t = int(input())

for _ in range(t):
    n = int(input())
    lst = ['2']
    if n== 1:
        print(-1)
    else:
        for i in range(n-1):
            lst.append('3')
        s = ''.join(lst)
        print(s)
            

