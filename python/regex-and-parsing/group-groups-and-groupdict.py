import re

s = raw_input()
result = re.search(r'([a-zA-Z0-9])\1+', s)

if (result):
        print(result.group(1))
    else:
        print(-1)
