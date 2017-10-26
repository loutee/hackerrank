#!/bin/python

import sys


q = int(raw_input().strip())
goal = 'hackerrank'
for a0 in xrange(q):
    s = raw_input().strip()
    index = 0
    for i in xrange(len(s)):
        if (index >= len(goal)):
            break
        if (s[i] == goal[index]):
            index += 1
    if (index == len(goal)):
        print('YES')
    else:
        print('NO')
