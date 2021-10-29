import numpy

n, m = map(int, input().split())

a = numpy.array([tuple(map(int, input().split())) for _ in range(n)])
b = numpy.array([tuple(map(int, input().split())) for _ in range(n)])

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

