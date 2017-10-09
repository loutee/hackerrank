#!/bin/python

import sys


t = int(raw_input().strip())
result = []
for a0 in xrange(t):
    n = int(raw_input().strip())
    h = 1
    for i in xrange(n):
        if (i % 2 == 1):
            h += 1
        else:
            h *= 2
    result.append(h)

for i in xrange(len(result)):
    print(result[i])
