import re

pattern = r'(?<!^)#[a-fA-F0-9]{3,6}'

n = int(raw_input())

result = []
for _ in xrange(n):
    s = raw_input()
    result += re.findall(pattern, s)

print("\n".join(x for x in result))
