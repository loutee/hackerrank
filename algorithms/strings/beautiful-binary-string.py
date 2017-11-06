#!/bin/python

import sys

def minSteps(n, B):
    count = 0
    while ('010' in B):
        i = B.find('010')
        B = B[0:i] + '011' + B[i+3:n]
        count += 1
    return count

n = int(raw_input().strip())
B = raw_input().strip()
result = minSteps(n, B)
print(result)
