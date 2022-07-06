#!/usr/bin/python3
import numpy as np

#(a) Create a two dimensional array called m1, shape=(4,5).
m1 = np.arange(20).reshape(4,5)
print(m1)
#(b) Create a new array m2 from m1, in which the elements of each row are in reverse order.
print(m1[:,::-1])

#(c) Create a new array m3 from m1, in which the elements of each column are in reverse order.
print(m1[::-1,:])

#(d) Cut of the first and last row and the first and last column of m1.
print(m1[1:-1,1:-1])
