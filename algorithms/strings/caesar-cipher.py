#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

result = ""
for i in xrange(n):
    current = ord(s[i])
    if (current >= 65 and current <= 90):
        current += (k%26)
        if (current > 90):
            current = (current%90)+64
    elif (current >= 97 and current <= 122):
        current += (k%26)
        if (current > 122):
            current = (current%122)+96
    result += chr(current)
print(result)
