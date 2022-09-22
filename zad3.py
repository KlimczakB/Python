#!/usr/bin/python3

import pandas as pd

n = pd.Series(['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'])
s = pd.Series(['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F','Ne'])
w = pd.Series([1, 4, 7, 9, 11, 12, 14, 16, 19, 20])


df=pd.DataFrame({'Name': n, 'Symbol': s, 'Weight': w})
df.index = range(1,11)
print(df)
