t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    result = set()
    for i in xrange(n):
        result.add(i*a+(n-1-i)*b)
    print(' '.join(str(x) for x in sorted(result)))
