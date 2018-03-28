import numpy

p = map(float, raw_input().split())
x = int(raw_input())

print(numpy.polyval(p, x))
