#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

max = 0
for i in xrange(n):
    uppercount = 0
    lowercount = 0
    for j in xrange(n):
        if (a[j] == a[i] or a[j] == a[i]+1):
            uppercount += 1
        if (a[j] == a[i] or a[j] == a[i]-1):
            lowercount -= 1
    if (uppercount > max):
        max = uppercount
    if (lowercount > max):
        max = lowercount
print(max)
