#!/usr/bin/python3

import numpy as np

#(a) Create an arbitrary one dimensional array called v1.
v1 = np.array( [1, 2, 4, 8, 16, 32] )
print(v1)

#(b) Create a new array v2 which consists of the odd indices of v1.
#v2 = v1[1::2] 
print(v1[1::2]) 

#(c) Create a new array v3 in backwards ordering from v1.
print(v1[::-1])
