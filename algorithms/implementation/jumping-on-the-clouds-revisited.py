#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
i = 0
energy = 100
while(energy > 0):
    i = (i+k)%n
    energy -= 1
    if (c[i] == 1):
        energy -= 2
    if (i == 0):
        break;
print(energy)
