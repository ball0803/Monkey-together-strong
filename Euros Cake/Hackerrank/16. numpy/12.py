import numpy

n = int(input())
a = []
for _ in range(n):
    row = map(int, input().split())
    a.append([*row])

b = []
for _ in range(n):
    row = map(int, input().split())
    b.append([*row])

np_a = numpy.matrix(a)
np_b = numpy.matrix(b)

print(numpy.dot(a, b))
