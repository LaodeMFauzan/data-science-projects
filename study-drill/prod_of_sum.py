import numpy as np

def get_product_of_sum(arr):
    return np.prod(np.sum(arr,axis = 0),axis = 0)

input_ = list(map(int,input().strip().split(' ')))
arr = np.array([input().split(' ') for _ in range(input_[0])], int)

print(get_product_of_sum(arr))