#!/usr/bin/python3

import math

n = 2022
x = format(math.pi, '.5f')
word = 'Python'
polish = 'książka'

with open('vars.txt', 'w') as outfile:
    outfile.write('{}\n{}\n{}\n{}'.format(n, x, word, polish))

with open('vars.txt', 'r') as outfile:
    text = outfile.read()

print(text)
