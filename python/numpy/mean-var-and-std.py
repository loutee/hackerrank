import numpy

n,m = map(int, raw_input().split())

arr = []
for _ in xrange(n):
    arr.append(map(int, raw_input().split()))

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr, axis=None))
