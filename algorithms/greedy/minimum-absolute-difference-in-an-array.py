#!/bin/python

import sys

def minimumAbsoluteDifference(n, arr):
    mini = 999
    arr = sorted(arr)
    for i in xrange(1,len(arr)):
        diff = abs(arr[i-1]-arr[i])
        if (diff < mini):
            mini = diff
        if (mini == 0):
            break
    return mini

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = minimumAbsoluteDifference(n, arr)
    print result
