import numpy as np

a,b = np.array(input().split(' '),int),np.array(input().split(' '),int)
print(np.inner(a,b),np.outer(a,b),sep = "\n")