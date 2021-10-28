import numpy

arr = numpy.array(tuple(i for i in map(int, input().split())))
arr = numpy.reshape(arr, (3, 3))
print(arr)
