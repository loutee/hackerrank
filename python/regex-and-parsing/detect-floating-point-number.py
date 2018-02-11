import re

t = int(raw_input())
pattern = re.compile('^[+-]?[0-9]*\.[0-9]+$')

for _ in xrange(t):
    n = raw_input()
    if (re.match(pattern, n)):
        print(True)
    else:
        print(False)
