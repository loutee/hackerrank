#!/bin/python

import sys


t = int(raw_input().strip())
result = []
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    count = 0
    for i in xrange(n):
        if (a[i] <= 0):
            count += 1
    if (count >= k):
        result.append("NO")
    else:
        result.append("YES")
for i in xrange(len(result)):
    print(result[i])
