#!/bin/python

import sys

def anagram(s):
    if (len(s)%2 == 1):
        return -1
    s1 = s[0:len(s)/2]
    s2 = list(s[len(s)/2:])
    for i in xrange(len(s)/2):
        if (s1[i] in s2):
            s2.pop(s2.index(s1[i]))
    return len(s2)

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagram(s)
    print(result)
