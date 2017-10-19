#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
d = []
for i in xrange(n-1):
    temp = A[i]
    A[i] = 0
    try:
        d.append(A.index(temp)-i)
    except:
        continue
if (d != []):
    print(min(d))
else:
    print(-1)
