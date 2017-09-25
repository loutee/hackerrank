#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    tallest = ar[0]
    for i in xrange(n):
        if (ar[i] > tallest):
            tallest = ar[i]
    count = 0
    for i in xrange(n):
        if (ar[i] == tallest):
            count += 1
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
