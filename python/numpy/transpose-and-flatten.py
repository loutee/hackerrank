import numpy

n,m = map(int, raw_input().split())
arr = []

for _ in xrange(n):
    arr.append(map(int, raw_input().split()))

arr = numpy.array(arr)
print(numpy.transpose(arr))
print(arr.flatten())
