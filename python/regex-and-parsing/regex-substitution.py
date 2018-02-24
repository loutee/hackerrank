import re

n = int(raw_input())

for _ in xrange(n):
    s = raw_input()
    result = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if (x.group() == '&&') else 'or', s)
    print(result)
