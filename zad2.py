#!/usr/bin/python3

#Generate n=100 random points in a unit square [0,1]x[0,1]. 
#Points are green if the distance from (0,0) is less then 1; they are red otherwise. 
#The marker area of a point (x,y) should be proportional to x+y.

import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.random.rand(n)
y = np.random.rand(n)

color = np.where(x**2 + y**2 < 1, 'g', 'r')

plt.scatter(x, y, s=25*(x + y), c=color)
plt.title('Exercise 9.2 - Random points')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
