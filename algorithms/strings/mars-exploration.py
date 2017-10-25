#!/bin/python

import sys


S = raw_input().strip()
count = 0

for i in range(0,len(S),3):
    if (S[i] != "S"):
        count += 1

for i in range(1,len(S),3):
    if (S[i] != "O"):
        count += 1

for i in range(2,len(S),3):
    if (S[i] != "S"):
        count += 1

print(count)
