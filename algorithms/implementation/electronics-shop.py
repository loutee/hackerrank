#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    # s: amount of money available
    # n: number of keyboards available for purchase
    # m: number of usbs available for purchase
    max = -1
    for i in xrange(n):
        for j in xrange(m):
            expense = keyboards[i] + drives[j]
            if (s-expense >= 0 and expense > max ):
                max = expense
    return max

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
