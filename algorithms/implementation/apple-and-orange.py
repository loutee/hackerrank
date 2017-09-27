#!/bin/python

import sys


# Start (s) and end (t) points of Sam's house
s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]

# Apple (a) and orange (b) tree location points
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]

# Number of apples (m) and oranges (n)
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]

# Distances from (a) and (b) of each apple or orange from respective trees
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

appleCount = 0
applePos = apple[:]
for i in xrange(m):
    applePos[i] += a
    if (applePos[i] >= s and applePos[i] <= t):
        appleCount += 1

orangeCount = 0
orangePos = orange[:]
for i in xrange(n):
    orangePos[i] += b
    if (orangePos[i] >= s and orangePos[i] <= t):
        orangeCount += 1

print appleCount
print orangeCount
