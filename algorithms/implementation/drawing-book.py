#!/bin/python

import sys

def solve(n, p):
    return min(p/2,n/2-p/2)

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)
