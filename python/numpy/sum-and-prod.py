import numpy

n,m = map(int, raw_input().split())

arr = []
for _ in xrange(n):
    arr.append(map(int, raw_input().split()))

print((numpy.prod(numpy.sum(arr, axis=0))))
