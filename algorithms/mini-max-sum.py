#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
temp = arr[:]
temp.pop(0)
min = sum(temp)
max = min

for i in xrange(len(arr)):
    temp = arr[:]
    temp.pop(i)
    result = sum(temp)
    if (result > max):
        max = result
    if (result < min):
        min = result
print str(min) + " " + str(max)
