#!/bin/python

import sys
import math


s = raw_input().strip()
max = int(math.ceil(math.sqrt(len(s))))
result = []
for i in xrange(max):
    result.append(s[i:len(s):max])
print(' '.join(result))
