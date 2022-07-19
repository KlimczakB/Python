#!/usr/bin/python3

#Plot functions sin(x), cos(x), and exp(-x) in a range [0,10]. 
#Colors are red, green, and blue, respectively. 
#Lines are solid, dashed, and dotted, respectively. Add a legend.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,200)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

plt.plot(x, y1, color='red', linestyle='solid', label='sin(x)')
plt.plot(x, y2,'g--', label='cos(x)')
plt.plot(x, y3, color='blue', linestyle='dotted', label='exp(-x)')
plt.title('Exercise 9.1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend() 
plt.show()
