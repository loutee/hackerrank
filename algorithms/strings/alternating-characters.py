#!/bin/python

import sys

def alternatingCharacters(s):
    count = 0
    for i in range(1,len(s)):
        if (s[i-1] == s[i]):
            count += 1
    return count

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = alternatingCharacters(s)
    print(result)
