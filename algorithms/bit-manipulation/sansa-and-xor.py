t = int(raw_input())

for _ in xrange(t):
    n = int(raw_input())
    a = map(int, raw_input().split(' '))
    if (n%2 == 0):
        print(0)
    else:
        print(reduce((lambda x,y: x^y), a[::2]))
