import re

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []

for _ in xrange(n):
    matrix.append(raw_input())

string = ""
for z in zip(*matrix):
    string += "".join(z)

pattern = "(?<=[A-Za-z0-9]{1})([!@#$%&\s]+)(?=[A-Za-z0-9]{1})"
print(re.sub(pattern, ' ', string))
