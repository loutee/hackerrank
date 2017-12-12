#!/bin/python

def maxXor(l,r):
    result = 0
    for i in xrange(l,r+1):
        for j in xrange(l,r+1):
            value = i^j
            if(value > result):
                result = value
    return result

l = int(raw_input());
r = int(raw_input());

res = maxXor(l,r);
print(res)
