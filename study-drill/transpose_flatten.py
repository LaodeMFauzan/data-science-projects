import numpy as np

matrix = list(map(int,(input().strip().split(' '))))

arr = []

for i in range(matrix[0]):
    arr = np.append(arr,[input().strip().split(' ')])
arr = list(map(int, arr))
arr = np.reshape(arr,(matrix[0],matrix[1]))
print(np.transpose(arr))
print(arr.flatten())