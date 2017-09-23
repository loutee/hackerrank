#!/bin/python

import sys

def aVeryBigSum(n, ar):
    total = 0
    for i in range (0, n):
        total += ar[i]
    return total

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
