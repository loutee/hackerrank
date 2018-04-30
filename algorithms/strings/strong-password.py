#!/bin/python

import sys
import re

numbers = r'^.*[0-9]+'
lower_case = r'^.*[a-z]+'
upper_case = r'^.*[A-Z]+'
spec_char = r'^.*[!@#$%\^&*()\-+]+'

def minimumNumber(n, password):
    length_diff = 6 - n
    strong_req = 0

    if (re.match(numbers, password) is None):
        strong_req += 1

    if (re.match(lower_case, password) is None):
        strong_req += 1

    if (re.match(upper_case, password) is None):
        strong_req += 1

    if (re.match(spec_char, password) is None):
        strong_req += 1

    return max(length_diff, strong_req)

if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    answer = minimumNumber(n, password)
    print answer
