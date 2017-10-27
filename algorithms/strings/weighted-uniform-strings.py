#!/bin/python

import sys


s = raw_input().strip()
n = int(raw_input().strip())

w = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l':12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

vals = set()
count = 1
old = ''
for i in xrange(len(s)):
    if (s[i] == old):
        count += 1
    else:
        count = 1
        old = s[i]
    vals.add(w[s[i]]*count)

for a0 in xrange(n):
    x = int(raw_input().strip())
    if (x in vals):
        print("Yes")
    else:
        print("No")
