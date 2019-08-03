import numpy as np


input_ = list(map(int,input().strip().split(' ')))

# this commented code only read one 1*N
# arr_1 = [list(map(int,input().split(' ') for _ in range(input_[0])))]

# arr_2 = [list(map(int,input().strip().split(' ')))]

a = np.array([input().split(' ') for num in range(input_[0])], int)
b = np.array([input().split(' ') for num in range(input_[0])], int)

print(a+b,a-b,a*b,a//b,a%b,a**b, sep="\n")