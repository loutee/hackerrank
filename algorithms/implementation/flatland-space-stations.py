#!/bin/python

import sys
import math


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))
c = sorted(c)
edgeL = False
edgeR = False
edgediffs = []
if (n-1 > c[-1]):
    c.append(n-1)
    m += 1
    edgeR = True
    edgediffs.append(c[m-1]-c[m-2])
if (0 != c[0]):
    c = [0] + c
    m += 1
    edgeL = True
    edgediffs.append(c[1]-c[0])
diffs = [0]
if (edgeR and edgeL):
    for i in range(2,m-1):
        diffs.append(c[i]-c[i-1])
elif (edgeR):
    for i in range(1,m-1):
        diffs.append(c[i]-c[i-1])
elif (edgeL):
    for i in range(2,m):
        diffs.append(c[i]-c[i-1])
else:
    for i in range(1,m):
        diffs.append(c[i]-c[i-1])

if (edgeL or edgeR):
    print(max(max(edgediffs),max(diffs)/2))
else:
    print(max(diffs)/2)
