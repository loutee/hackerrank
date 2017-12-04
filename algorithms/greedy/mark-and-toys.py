#!/bin/python

import sys

def maximumToys(prices, k):
    plist = sorted(prices)
    m = k
    count = 0
    while (plist != []):
        if (m>=plist[0]):
            m = m-plist.pop(0)
            count += 1
        else:
            break
    return count

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k)
    print result
