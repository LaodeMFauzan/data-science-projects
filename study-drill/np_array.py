import numpy

def arrays(arr):
    arr_np = numpy.array(arr,float)
    return (numpy.flip(arr_np))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)