import numpy

n = int(input())

arr = []
for _ in range(n):
    row = input().split()
    arr.append(row)

matrix = numpy.matrix(arr, dtype=float)
print(round(numpy.linalg.det(matrix), 2))
