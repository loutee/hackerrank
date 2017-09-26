#!/bin/python

import sys

def timeConversion(s):
    # hh:mm:ssPM
    # 0123456789
    # Fails on test case 4 for unknown reason
    # hour = int(s[0:2])
    # if (s[8:] == "PM" and hour != "12"):
    #     hour += 12
    # elif (s[8:] == "AM"):
    #     if (hour == 12):
    #         hour = 0
    # hour = str(hour)
    # if (len(hour) == 1):
    #     hour = "0" + hour
    # return hour+":"+s[3:5]+":"+s[6:8]

    hour, min, sec = map(int, s[:-2].split(':'))
    p = s[-2:]
    hour = hour % 12 + (p.upper() == 'PM') * 12
    return (('%02d:%02d:%02d') % (hour, min, sec))

s = raw_input().strip()
result = timeConversion(s)
print(result)
