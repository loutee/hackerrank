import re

n = int(raw_input())

pattern = "^[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}$"

for _ in xrange(n):
    name, email = raw_input().split()
    if (re.match(pattern, email[1:-1])):
        print(name + " " + email)
