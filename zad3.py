#!/usr/bin/python3

import random

def random_walk(start): 
    result = [start]
    pos = start
    for _ in range(100):
        pos += random.choice([1, -1])
        result.append(pos)
    return result

print(random_walk(0))
