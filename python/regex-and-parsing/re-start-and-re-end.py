import re

s = raw_input()
k = raw_input()

pattern = re.compile(k)
result = pattern.search(s)

if (result):
    while (result):
        print("({0}, {1})".format(result.start(), result.end() - 1))
        result = pattern.search(s, result.start() + 1)
else:
    print("(-1, -1)")
