#!/bin/python

import sys


Q = int(raw_input().strip())
for a0 in xrange(Q):
    n = int(raw_input().strip())
    b = raw_input().strip()
    count = [0]*26
    us = False
    for i in xrange(n):
        if (b[i] != '_'):
            count[ord(b[i])-65] += 1
        else:
            us = True
    valid = True
    for i in xrange(26):
        if (count[i] == 1):
            valid = False
            break
    if (valid and us):
        print('YES')
    elif (valid):
        temp = list(b)
        old = ''
        while (temp != []):
            if (len(temp)>1 and temp[0] == temp[1]):
                old = temp.pop(0)
                temp.pop(0)
            else:
                if (temp[0] == old):
                    temp.pop(0)
                else:
                    valid = False
                    break
        if (valid):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
