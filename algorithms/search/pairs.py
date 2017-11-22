#!/usr/bin/py
def pairs(a,k):
    return (len(set(a).intersection(set(x + k for x in a))))

n,k = raw_input().split(' ')
n,k = [int(n),int(k)]
a = map(int, raw_input().split(' '))
print pairs(a,k)
