import numpy

n = int(raw_input())

arr = []
for _ in xrange(n):
    arr.append(map(float, raw_input().split()))

print(numpy.linalg.det(arr))
