import numpy

def arrays(arr):
    
    rev = list(reversed(arr))
    return numpy.array(rev, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
