n = int(raw_input())
orders = []
for i in range(1,n+1):
    t,d = raw_input().split(' ')
    t,d = [int(t),int(d)]
    orders.append([t+d,i])
orders.sort()
print(' '.join(str(x[1]) for x in orders))
