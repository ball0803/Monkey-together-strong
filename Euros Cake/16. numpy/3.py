import numpy

n, _ =  map(int, input().split())
arr = []
for _ in range(n):
    k = [*map(int, input().split())]
    arr.append(k)

np_arr = numpy.array(arr)
print(numpy.transpose(np_arr))
print(np_arr.flatten())


