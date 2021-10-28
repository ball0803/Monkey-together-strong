import numpy

numpy.set_printoptions(sign=' ')

arr = numpy.array([*map(float, input().split())])

print(numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr), sep='\n')
