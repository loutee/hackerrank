#!/bin/python

import sys

def super_reduced_string(s):
    result = ['']
    for i in xrange(len(s)):
        if (result[-1] == s[i]):
            result.pop()
        else:
            result.append(s[i])
    if (result != ['']):
        return ''.join(result)
    else:
        return "Empty String"

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
