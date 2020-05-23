from collections import deque
n = int(input())
d = deque()
for i in range(n):
    s = input()
    if s == 'pop':
        d.pop()
    elif s == 'popleft':
        d.popleft()    
    else:    
        command, num = map(str, s.split())
        num = int(num)
        getattr(d, command)(num)
print(" ".join(map(str, d)))    