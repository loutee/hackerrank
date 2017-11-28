#!/bin/python

import sys


t = int(raw_input().strip())

st = 1
count = -1
while (st <= t):
    count += 1
    old = st
    st = (st+1)*2
print(3*(2**count)-(t-old))
