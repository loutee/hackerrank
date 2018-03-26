import numpy

n = int(raw_input())

arrA = []
for _ in xrange(n):
    arrA.append(map(int, raw_input().split()))

arrB = []
for _ in xrange(n):
    arrB.append(map(int, raw_input().split()))

print(numpy.dot(arrA, arrB))

