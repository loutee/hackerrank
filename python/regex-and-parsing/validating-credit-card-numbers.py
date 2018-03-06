import re

pattern = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})" # Must not have 4 or more consecutive repeated digits
    r"[456]"               # Must begin with a 4, 5, or 6
    r"\d{3}"               # Followed by three digits 0-9
    r"(?:-?\d{4}){3}"      # Followed by three groups of 4 digits, optionally hyphens
    r"$")

n = int(raw_input())

for _ in xrange(n):
    s = raw_input()
    if (re.match(pattern, s)):
        print('Valid')
    else:
        print('Invalid')
