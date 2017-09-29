#!/bin/python

import sys

def getRecord(s):
    lowest = s[0]
    highest = s[0]
    lowBreaks = 0
    highBreaks = 0
    for i in range(1, n):
        if (s[i] > highest):
            highest = s[i]
            highBreaks += 1
        elif (s[i] < lowest):
            lowest = s[i]
            lowBreaks += 1
    return [highBreaks, lowBreaks]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
