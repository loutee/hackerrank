#!/bin/python

import sys

def makingAnagrams(s1, s2):
    both = list(set(s1).intersection(set(s2)))
    s1 = list(s1)
    s2 = list(s2)
    for i in xrange(len(both)):
        while (both[i] in s1 and both[i] in s2):
            s1.pop(s1.index(both[i]))
            s2.pop(s2.index(both[i]))
    return (len(s1)+len(s2))

s1 = raw_input().strip()
s2 = raw_input().strip()
result = makingAnagrams(s1, s2)
print(result)
