#!/bin/python

import sys

def compare(a, b):
    if (a > b):
        return [1, 0]
    elif (a < b):
        return [0, 1]
    else:
        return [0, 0]

def solve(a0, a1, a2, b0, b1, b2):
    alice = 0
    bob = 0
    result0 = compare(a0, b0)
    result1 = compare(a1, b1)
    result2 = compare(a2, b2)
    alice += (result0[0] + result1[0] + result2[0])
    bob += (result0[1] + result1[1] + result2[1])
    return [alice, bob]

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
