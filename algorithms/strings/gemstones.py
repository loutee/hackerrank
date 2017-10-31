#!/bin/python

import sys

def gemstones(arr):
    result = set(arr[0])
    for i in xrange(1,len(arr)):
        result = result.intersection(set(arr[i]))
    return len(result)

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
