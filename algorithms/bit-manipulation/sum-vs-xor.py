#!/bin/python

import sys

def solve(n):
    if (n == 0):
        return 1
    count = 0
    b = '{0:b}'.format(n)
    for i in xrange(len(b)):
        if (b[i] == '0'):
            count += 1
    return (2**count)

n = long(raw_input().strip())
result = solve(n)
print(result)
