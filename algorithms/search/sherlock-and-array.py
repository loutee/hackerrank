#!/bin/python

import sys

def solve(a):
    if (len(a) == 1):
        return "YES"
    right = sum(a)
    left = 0
    for i in xrange(len(a)):
        right -= a[i]
        if (left == right):
            return "YES"
        left += a[i]
    return "NO"

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)
