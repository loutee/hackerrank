#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    if (len(s) == 1):
        print('NO')
    else:
        first = []
        for i in range(1,len(s)/2+1):
            first.append(s[0:i])
        for j in xrange(len(first)):
            next = first[j]
            valid = True
            i = len(first[j])
            while (i < len(s)):
                next = str(int(next)+1)
                if (s[i:i+len(next)] != next):
                    valid = False
                    break
                i += len(next)
            if (valid):
                print('YES ' + first[j])
                break
        if (valid == False):
            print 'NO'
