#!/bin/python

import sys

def isValid(s):
    alphacount = [0]*26
    for i in xrange(len(s)):
        alphacount[ord(s[i])-97] += 1
    freqs = list(set(alphacount))
    if (0 in freqs):
        freqs.remove(0)
    if (len(freqs) == 1):
        return 'YES'
    elif (len(freqs) == 2):
        a = alphacount[:]
        b = alphacount[:]
        a[a.index(freqs[0])] -= 1
        b[b.index(freqs[1])] -= 1
        afreqs = list(set(a))
        bfreqs = list(set(b))
        if (0 in afreqs):
            afreqs.remove(0)
        if (0 in bfreqs):
            bfreqs.remove(0)
        if (len(afreqs) == 1 or len(bfreqs) == 1):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


s = raw_input().strip()
result = isValid(s)
print(result)
