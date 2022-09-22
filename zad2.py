#!/usr/bin/python3
import pandas as pd
import random

temp = []
for i in range(1,32):
    temp.append(random.randrange(25,40))

s=pd.Series(index=range(1,32), data=temp)
print(s)

