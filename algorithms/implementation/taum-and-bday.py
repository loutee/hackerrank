#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    total = 0
    if (x < y+z):
        total += (b*x)
    else:
        total += b*(y+z)
    if (y < x+z):
        total += (w*y)
    else:
        total += w*(x+z)
    print(total)
