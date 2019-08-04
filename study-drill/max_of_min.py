import numpy as np

def get_min_of_max(arr):
    return np.max(np.min(arr,axis = 1),axis = None)

size = list(map(int,input().split(' ')))

arr = np.array([input().split(' ') for _ in range(size[0])],int)

print(get_min_of_max(arr))