t = int(raw_input())

for _ in xrange(t):
    a,b = raw_input().split()
    try:
        print(int(a)/int(b))
    except Exception as e:
        print "Error Code:",e
