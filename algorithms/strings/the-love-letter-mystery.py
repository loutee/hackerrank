#!/bin/python

import sys

def theLoveLetterMystery(s):
    r = list(s[::-1])
    s = list(s)
    count = 0
    for i in range(0,len(s)/2):
        if (s[i] != r[i]):
            if (s[i] > r[i]):
                count += ord(s[i])-ord(r[i])
                s[i] = r[i]
            else:
                count += ord(r[i])-ord(s[i])
                r[i] = s[i]
    return count

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)
