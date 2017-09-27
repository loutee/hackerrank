#!/bin/python

import sys

def solve(grades):
    # Complete this function
    for i in xrange(n):
        if (grades[i] >= 38):
            div = grades[i]/5
            div = 5*(div+1)
            if ((div - grades[i]) < 3):
                grades[i] = div
    return grades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
