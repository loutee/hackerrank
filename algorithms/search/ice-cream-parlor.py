# Trips to the parlor
t = int(raw_input())

for i in xrange(t):
    # Dollars available to spend
    m = int(raw_input())

    # Number of flavors
    n = int(raw_input())

    # Cost of each respective flavor
    cost = map(int, raw_input().split(' '))

    for j in xrange(n):
        if (m-cost[j] in cost):
            if (m-cost[j] == cost[j]):
                if (m-cost[j] in cost[j+1:]):
                    print(str(j+1) + ' ' + str(j+1 + cost[j+1:].index(m-cost[j])+1))
                    break
                else:
                    continue
            print(str(j+1) + ' ' + str(cost.index(m-cost[j])+1))
            break
