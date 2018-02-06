#!/bin/python

import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in xrange(n):
        arr_temp = map(int,raw_input().strip().split(' '))
        arr.append(arr_temp)
    k = int(raw_input().strip())

    arr = sorted(arr, key=lambda athlete_details: athlete_details[k])
    for i in xrange(n):
        print(" ".join(str(x) for x in arr[i]))
