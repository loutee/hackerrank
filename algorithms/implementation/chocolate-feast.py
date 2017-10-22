#!/bin/python

import sys

def unwrap(choco,m,r):
    if(choco != 0):
        return ((choco+r)/m + unwrap(choco/m,m,choco%m))
    else:
        return 0


t = int(raw_input().strip())
wraps = 0
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    count = n/c + unwrap(n/c,m,0)
    print(count)
