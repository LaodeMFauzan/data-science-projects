import numpy

def reshape(arr):
    arr_reshape = numpy.array(arr,int)
    return numpy.reshape(arr_reshape,(3,3))

arr = input().strip().split(' ')
result = reshape(arr)
print(result)

