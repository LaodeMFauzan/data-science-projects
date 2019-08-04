import numpy as np
np.set_printoptions(sign=' ')

def get_result(arr):
    print(np.mean(arr,axis = 1))
    print(np.var(arr,axis = 0))
    std = round(np.std(arr,axis = None),12)
    print(std)

input_ = list(map(int,input().strip().split(' ')))
arr = np.array([input().split(' ') for _ in range(input_[0])], int)

get_result(arr)