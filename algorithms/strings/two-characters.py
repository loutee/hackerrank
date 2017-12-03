#!/bin/python

n = int(raw_input())
s = raw_input()

c = sorted(list(set(s)))
c_len = len(c)
chars = []
lengths = []
for i in xrange(c_len):
    chars.append(['']*c_len)
    lengths.append([0]*c_len)
for i in xrange(n):
    for j in xrange(c_len):
        current = c.index(s[i])
        if (chars[current][j] != s[i] and chars[current][j] != 'X'):
            chars[current][j] = s[i]
            lengths[current][j] += 1
        else:
            chars[current][j] = 'X'
            lengths[current][j] = 0

        if (chars[j][current] != s[i] and chars[j][current] != 'X'):
            chars[j][current] = s[i]
            lengths[j][current] += 1
        else:
            chars[j][current] = 'X'
            lengths[j][current] = 0
result = 0
for i in xrange(c_len):
    rmax = max(lengths[i])
    if (result < rmax):
        result = rmax
print(result)
