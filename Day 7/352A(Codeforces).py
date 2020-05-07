n = int(input())
a = input()
arr = [int(y) for y in a.split()]
count5 = arr.count(5)
count0 = arr.count(0)
arr5 = [5]
arr0 = [0]

x = count5//9 

if x >=1 and count0 >0:
    b = arr5*(x*9)
    c = arr0*count0
    final_arr = b+c
    for i in final_arr:
        print(i,end='')
elif count0 == 0:
    print(-1)
else:
    print(0)


