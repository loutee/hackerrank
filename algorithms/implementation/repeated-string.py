#!/bin/python

import sys

s = raw_input().strip()
n = long(raw_input().strip())
count = 0
for i in xrange(len(s)):
    if (s[i] == 'a'):
        count += 1
remain = n % len(s)
count = count * (n/len(s))
for i in xrange(remain):
    if (s[i] == 'a'):
        count += 1
print(count)
