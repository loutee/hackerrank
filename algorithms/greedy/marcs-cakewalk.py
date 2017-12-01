#!/bin/python

import sys


n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
calories = sorted(calories,reverse=True)
miles = 0
for i in xrange(n):
    miles += (calories[i]*2**i)
print(miles)
