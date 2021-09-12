import numpy
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input().split())

np_arr = numpy.array(arr, dtype=int)

print(numpy.mean(np_arr, axis=1), numpy.var(np_arr, axis=0), round(numpy.std(np_arr), 11), sep='\n')
