#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    fives = n
    while(fives%3 != 0):
        fives -= 5
    if (fives<0):
        print('-1')
    else:
        print(fives*str(5)+(n-fives)*str(3))
