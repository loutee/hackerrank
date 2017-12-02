t = int(raw_input())

for _ in xrange(t):
    n = int(raw_input())
    g = []
    for i in xrange(n):
        g.append(sorted(list(raw_input())))
    valid = True
    for i in range(1,n):
        for j in xrange(n):
            if (g[i][j] < g[i-1][j]):
                valid = False
                break
    if (valid):
        print('YES')
    else:
        print('NO')
