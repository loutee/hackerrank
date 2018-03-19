import numpy

vals = tuple(map(int, raw_input().split()))
print(numpy.zeros(vals, dtype = numpy.int))
print(numpy.ones(vals, dtype = numpy.int))
