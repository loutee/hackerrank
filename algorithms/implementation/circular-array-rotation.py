#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
new = []
for i in xrange(n):
    new.append(a[-(k%n)+i])
for a0 in xrange(q):
    m = int(raw_input().strip())
    print(new[m])
