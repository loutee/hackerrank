#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
position = 0
count = 0
while (position < n-1):
    if (position+2 < n and c[position+2] == 0):
        position += 2
    else:
        position += 1
    count += 1
print(count)
