#!/bin/python

import sys


s = raw_input().strip()
print(sum(map(str.isupper,s))+1)
