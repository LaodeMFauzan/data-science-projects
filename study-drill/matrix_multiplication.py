import numpy as np

input_ = list(map(int,input().strip().split(' ')))

a = np.array([input().split(' ') for num in range(input_[0])], int)
b = np.array([input().split(' ') for num in range(input_[0])], int)

c = a.dot(b)
print(c)