#!/bin/python

import sys

def getMinimumCost(n, k, c):
    c = sorted(c, reverse=True)
    result = 0
    i = 0
    x = 0
    while (c != []):
        if (i == k):
            i = 0
            x += 1
        result += (x+1)*c.pop(0)
        i += 1
    return result


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
c = map(int, raw_input().strip().split(' '))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)
