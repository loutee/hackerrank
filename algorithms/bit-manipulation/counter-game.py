def powerOf2(n):
    b = '{0:b}'.format(n)[1:]
    for i in xrange(len(b)):
        if (b[i] == '1'):
            return False
    return True

def highestPowerOf2(n):
    b = '{0:b}'.format(n)
    b = '1'+'0'*(len(b)-1)
    return int(b,2)

t = int(raw_input())

for _ in xrange(t):
    n = int(raw_input())
    louise = False
    while (n>1):
        louise = not louise
        if (powerOf2(n)):
            n -= n/2
        else:
            n -= highestPowerOf2(n)
    if (louise):
        print('Louise')
    else:
        print('Richard')
