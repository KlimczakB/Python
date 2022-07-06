#!/usr/bin/python3
 
import random
import itertools

iter_a = itertools.cycle([0, 1])

def iter_b():
    while True:
        yield random.choice([0, 1])

iter_c = itertools.cycle([0, 1, 0, -1])

a = iter_a
b = iter_b()
c = iter_c

for x in range(15):
    print( '{}  {}  {}'.format(next(a), next(b), next(c)) )


