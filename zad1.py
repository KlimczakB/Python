#!/usr/bin/python3

import numpy as np 

#Create the following NumPy arrays:
#(a) float from 0.0 to 1.0 step 0.1, shape=(11,),
a = np.arange(0, 1.1, 0.1).reshape(11, )

#(b) int zeros (1 byte) with shape=(5,6),
b = np.zeros((5, 6), dtype='int8')

#(c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8.
#w Pythonie jednostką urojoną jest j, a nie i
c = np.power(1J, np.arange(9))

print('NumPy array:')
print('a) ', a)
print('b) ')
print(b)
print('c) ', c)
