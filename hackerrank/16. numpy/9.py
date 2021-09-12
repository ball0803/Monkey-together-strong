import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], dtype=int)
print(numpy.prod(numpy.sum(arr, axis=0)))
