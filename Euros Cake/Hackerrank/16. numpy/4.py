import numpy

n, m , p = map(int ,input().split())
n_arr = numpy.array([input().split() for _ in range(n)], int)
m_arr = numpy.array([input().split() for _ in range(m)], int)
print(numpy.concatenate((n_arr, m_arr), axis=0))
