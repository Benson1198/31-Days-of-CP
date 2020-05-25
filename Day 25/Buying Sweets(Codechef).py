for tc in range(int(input())):
    
    n,x = map(int,input().split(' '))
    
    li = list(map(int,input().split()))
    
    li.sort()
    
    if sum(li)//x == sum(li[1:])//x:
        print(-1)
    else:
        print(sum(li)//x)