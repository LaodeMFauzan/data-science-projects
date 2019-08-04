import numpy as np
np.set_printoptions(sign=' ')

input_ = list(map(float,input().split(' ')))

print(np.floor(input_),np.ceil(input_),np.rint(input_),sep = "\n")