#!/bin/python

import sys


def kangaroo(x1, v1, x2, v2):
    if ((x2 > x1 and v2 > v1) or v1 == v2):
        return "NO"
    jumps = (x2-x1)/(v1-v2)
    if (jumps < 0):
        return "NO"
    res1 = v1*jumps + x1
    res2 = v2*jumps + x2
    if (res1 == res2):
        return "YES"
    else:
        return "NO"

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
