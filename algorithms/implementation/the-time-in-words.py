#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())
w = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine']

if (m == 0):
    print(w[h-1] + " o' clock")
elif (m == 1):
    print('one minute past ' + w[h-1])
elif (m < 15):
    print(w[m-1] + ' minutes past ' + w[h-1])
elif (m == 15):
    print('quarter past ' + w[h-1])
elif (m < 30):
    print(w[m-1] + ' minutes past ' + w[h-1])
elif (m == 30):
    print('half past ' + w[h-1])
elif (m < 45):
    print(w[60-m-1] + ' minutes to ' + w[h%12])
elif (m == 45):
    print('quarter to ' + w[h%12])
elif (m < 59):
    print(w[60-m-1] + ' minutes to ' + w[h%12])
else:
    print('one minute to ' + w[h%12])
