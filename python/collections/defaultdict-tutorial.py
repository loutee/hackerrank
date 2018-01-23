from collections import defaultdict

n, m = list(map(int, raw_input().split()))
d = defaultdict(list)

for i in xrange(n):
    d[raw_input()].append(i + 1)

for i in xrange(m):
    print(" ".join(map(str, d[raw_input()])) or -1)
