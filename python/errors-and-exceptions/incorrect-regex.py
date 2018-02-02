import re

t = int(raw_input())

for _ in xrange(t):
    regex = raw_input()
    try:
        re.compile(regex)
        print(True)
    except:
        print(False)
