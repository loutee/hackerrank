#!/bin/python

import sys

def solve(year):
    # Days from January to September excluding February
    count = 215
    feb = 28
    if ((year >= 1700) and (year <= 1917) and (year % 4 == 0)):
        # 1700-1917: Julian calendar
        feb = 29
    elif (year == 1918):
        # 1918: Transitionary calendar
        return "26.09.1918"
    else:
        # 1919-present: Gregorian calendar
        if ((year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0))):
            feb = 29
    count += feb
    day = 256 - count
    return str(day) + ".09." + str(year)

year = int(raw_input().strip())
result = solve(year)
print(result)
