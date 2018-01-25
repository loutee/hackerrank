from collections import OrderedDict

dict = OrderedDict()
n = int(raw_input())

for i in xrange(n):
    line = raw_input().split()
    item_name = " ".join(line[:-1])
    net_price = int(line[-1])
    try:
        dict[item_name] += net_price
    except:
        dict[item_name] = net_price

for key, value in dict.items():
    print(key + " " + str(value))
