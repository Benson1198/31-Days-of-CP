f_line = input().split()

t = int(f_line[0])
sx = int(f_line[1])
sy = int(f_line[2])
ex = int(f_line[3])
ey = int(f_line[4])

dx = ex-sx
dy = ey-sy

tx = 0
ty = 0

dir_lst = list(input())
min_time = 0

for i in dir_lst:
    if dx == tx and dy == ty:
        break
    else:
        min_time += 1
        if i == 'E':
            if dx <= 0:
                continue
            else:
                tx += 1
        elif i == 'S':
            if dy >= 0:
                continue
            else:
                ty -= 1
        elif i == 'W':
            if dx >= 0:
                continue
            else:
                tx -= 1
        elif i == 'N':
            if dy <= 0:
                continue
            else:
                ty += 1
if dx == 0 and dy == 0:
    print(0)
elif dx != tx or dy != ty:
    print(-1)
else:
    print(min_time)