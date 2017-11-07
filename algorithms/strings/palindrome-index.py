#!/bin/python

import sys

def palindromeIndex(s):
    if (s == s[::-1]):
        return -1
    for i in xrange(len(s)/2):
        if (s[i] != s[-1-i]):
            t = s[0:i]+s[i+1:]
            r = s[0:len(s)-1-i]+s[len(s)-i:]
            if (t == t[::-1]):
                return i
            elif (r == r[::-1]):
                return len(s)-1-i
    return -1


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = palindromeIndex(s)
    print(result)
