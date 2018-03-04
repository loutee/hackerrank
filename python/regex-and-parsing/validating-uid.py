import re

p1 = r'(?:([A-Za-z0-9])(?!.*\1)){10}'
p2 = r'(.*[A-Z].*){2,}'
p3 = r'(.*[0-9].*){3,}'

t = int(raw_input())

for _ in xrange(t):
    s = raw_input()

    if (re.match(p1, s) and re.match(p2, s) and re.match(p3, s)):
        print('Valid')
    else:
        print('Invalid')
