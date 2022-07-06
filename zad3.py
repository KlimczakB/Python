#!/usr/bin/python3

def iter_even():
    x = 0
    while True:
        yield x
        x = x + 2

def iter_odd():
    x = 1
    while True:
        yield x
        x = x + 2

def iter_power(k):
    x = 1
    while True:
        yield x
        x = x * k

even = iter_even()
odd = iter_odd()
power = iter_power(2)

for x in range(15):
    print( '{} {} {}'.format(next(even), next(odd), next(power)) )


