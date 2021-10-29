from collections import OrderedDict

t = int(input())
d = OrderedDict()
for _ in range(t):
    *item, price = input().split()
    name =  ' '.join(item)
    if not name in d:
        d[name] = int(price)
    else:
        d[name] += int(price)
for name, val in d.items():
    print(name, val)    
