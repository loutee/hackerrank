#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = 0
highest = 0
for i in xrange(len(word)):
    current = h[letters.index(word[i])]
    if (highest < current):
        highest = current
print(highest*len(word))
