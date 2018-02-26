import re

pattern = re.compile(r'^[7-9]{1}[0-9]{9}$')

n = int(raw_input())

for _ in xrange(n):
    s = raw_input()
    if re.match(pattern, s):
        print("YES")
    else:
        print("NO")
