#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    string = str(n)
    count = 0
    for i in xrange(len(string)):
        if (string[i] != '0'):
            if (n % int(string[i]) == 0):
                count += 1
    print(count)
