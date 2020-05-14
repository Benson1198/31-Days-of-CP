def stepCounter(n):
    step_sum = 0
    for i in range(3,n+1,2):
        ele_num = (i)+(i-1)+(i-1)+(i-2)
        step_sum += ele_num * (int(i/2))
    return step_sum


t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
    elif n>1:
        print(stepCounter(n))