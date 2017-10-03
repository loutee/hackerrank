#!/bin/python

import sys

def sockMerchant(n, ar):
    count = 0
    socks = [0] * 100
    for i in xrange(n):
        socks[ar[i]-1] += 1
    for j in range(0,100):
        count += socks[j]/2
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
