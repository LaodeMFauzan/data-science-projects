import numpy as np

input_ = input().strip().split(' ')

arr,arr_2 = [],[]
for i in range(int(input_[0])):
    arr = np.append(arr,[input().strip().split(' ')])
arr = list(map(int, arr))
arr = np.reshape(arr,(int(input_[0]),int(input_[2])))

for i in range(int(input_[1])):
    arr_2 = np.append(arr_2,[input().strip().split(' ')])
arr_2 = list(map(int, arr_2))
arr_2 = np.reshape(arr_2,(int(input_[1]),int(input_[2])))

print(np.concatenate((arr,arr_2),axis = 0))