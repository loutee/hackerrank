#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

diag1 = 0
diag2 = 0
for i in xrange(n):
    diag1 += a[i][i]
    diag2 += a[i][-(i+1)]
result = diag1 - diag2
print abs(result)
