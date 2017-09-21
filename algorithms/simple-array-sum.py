#!/bin/python

import sys

def simpleArraySum(n, ar):
  total = 0
  for i in range(0, n):
    total += ar[i]
  return total

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)

