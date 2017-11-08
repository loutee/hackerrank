#!/bin/python

import sys

def gameOfThrones(s):
    alphacount = [0]*26
    for i in xrange(len(s)):
        alphacount[ord(s[i])-97] += 1
    oddcount = 0
    for i in xrange(26):
        if (alphacount[i]%2 == 1):
            if (oddcount > 1):
                return 'NO'
            oddcount += 1
    return 'YES'


s = raw_input().strip()
result = gameOfThrones(s)
print(result)
