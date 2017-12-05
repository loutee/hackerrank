n = int(raw_input())
w = sorted(map(int, raw_input().split(' ')))
lb = w[0]
rb = lb+4
units = 1
for i in xrange(n):
    if (w[i] >= lb and w[i] <= rb):
        continue
    else:
        units += 1
        lb = w[i]
        rb = lb+4
print(units)
