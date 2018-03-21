import numpy

n,m = map(int, raw_input().split())

a = []
b = []

for _ in xrange(n):
    a.append(map(int, raw_input().split()))

for _ in xrange(n):
    b.append(map(int, raw_input().split()))

a = numpy.array(a)
b = numpy.array(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
