import numpy

n,m,p = map(int, raw_input().split())

arr1 = []
for _ in xrange(n):
    arr1.append(map(int, raw_input().split()))

arr2 = []
for _ in xrange(m):
    arr2.append(map(int, raw_input().split()))

print(numpy.concatenate((arr1, arr2)))
