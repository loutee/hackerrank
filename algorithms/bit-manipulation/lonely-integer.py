#!/bin/python

import sys

def lonelyinteger(a):
    result = a[0]
    for i in range(1,len(a)):
        result = result^a[i]
    return result

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = lonelyinteger(a)
print(result)
