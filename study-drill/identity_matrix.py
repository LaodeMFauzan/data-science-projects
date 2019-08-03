import numpy as np
np.set_printoptions(sign=' ')

def get_eye(size):
    return (np.eye(size[0],size[1],k=0))

size = list(map(int,input().split(' ')))

print(get_eye(size))