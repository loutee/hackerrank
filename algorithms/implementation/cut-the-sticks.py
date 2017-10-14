#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while (len(arr) != 0):
    short = min(arr)
    count = 0
    zeros = 0
    # Cut
    for i in xrange(len(arr)):
        arr[i] = arr[i] - short
        count += 1
        if (arr[i] == 0):
            zeros += 1
    # Remove 0s
    for i in xrange(zeros):
        arr.remove(0)
    print(count)
