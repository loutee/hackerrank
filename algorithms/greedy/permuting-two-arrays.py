q = int(raw_input())
for _ in xrange(q):
    n,k = raw_input().split(' ')
    n,k = [int(n),int(k)]
    a = map(int, raw_input().split(' '))
    b = map(int, raw_input().split(' '))
    for i in xrange(n):
        b[i] = k-b[i]
    a.sort()
    b.sort()
    valid = True
    for i in xrange(n):
        if (a[i] < b[i]):
            valid = False
            break
    if (valid):
        print('YES')
    else:
        print('NO')
