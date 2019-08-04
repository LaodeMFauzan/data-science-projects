import numpy as np

def get_val(pol,pos):
    return np.polyval(pol,pos)

pol = np.array(input().split(' '),float)
pos = int(input())

print(get_val(pol,pos))