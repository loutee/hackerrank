#!/bin/python

import sys

def funnyString(s):
    r = s[::-1]
    for i in range(1,len(s)):
        if(abs(ord(s[i])-ord(s[i-1])) != abs(ord(r[i])-ord(r[i-1]))):
            return "Not Funny"
    return "Funny"


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)
