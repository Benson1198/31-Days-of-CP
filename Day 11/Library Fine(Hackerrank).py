def libraryFine(d1, m1, y1, d2, m2, y2):
    if ((y1<y2) or (m1<m2) and (y1==y2)):
        return 0
    elif (m1<=m2 and y1<=y2):
        if d1<=d2:
            return 0
        elif d1>d2:
            return 15*abs(d1-d2)
    
    elif y1==y2:
        if m1>m2:
            return 500*abs(m1-m2)
    else:
        return 10000

s1 = input().split()
s2 = input().split()

d1 = int(s1[0])
m1 = int(s1[1])
y1 = int(s1[2])

d2 = int(s2[0])
m2 = int(s2[1])
y2 = int(s2[2])

print(libraryFine(d1, m1, y1, d2, m2, y2))