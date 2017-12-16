t = int(raw_input())

for _ in xrange(t):
    x = int(raw_input())
    x = ('{0:032b}'.format(x))
    result = ''
    for i in xrange(32):
        if (x[i] == '1'):
            result += '0'
        else:
            result += '1'
    print(int(result,2))
