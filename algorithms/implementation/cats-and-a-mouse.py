#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    A = abs(x - z)
    B = abs(y - z)
    if (A < B):
        print("Cat A")
    elif (A > B):
        print("Cat B")
    else:
        print("Mouse C")
