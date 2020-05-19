from collections import OrderedDict
d = OrderedDict()

for _ in range (int(input())):
    data = list(map(str,input().split()))
    try:
        item_name = data[0]
        net_price = int(data[1])
    except Exception :
        item_name = data[0] + ' ' + data[1]
        net_price = int(data[2])
   
    if d.get(item_name):
            d[item_name] += net_price
    else:
        d[item_name] = net_price

for i,v in d.items():
    print(i,v)