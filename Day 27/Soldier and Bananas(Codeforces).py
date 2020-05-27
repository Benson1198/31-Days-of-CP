k,n,w = [int(y) for y in input().split()]

total_cost = 0

for i in range(1,w+1):
    total_cost += i*k

to_borrow = total_cost-n

if to_borrow< 0:
    print(0)
else:
    print(to_borrow)