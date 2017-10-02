#!/bin/python

import sys

def migratoryBirds(n, ar):
    count = [0, 0, 0, 0 ,0]
    #  ID =  1, 2, 3, 4, 5
    for i in xrange(n):
        count[ar[i]-1] += 1
    highest = 1
    for i in range(1,5):
        if (count[highest-1] < count[i]):
            highest = i+1
    return highest

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
