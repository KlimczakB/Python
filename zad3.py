#!/usr/bin/python3

#1
print(sum(b*b for b in range(1, 2022, 2)))

#2
def sum(n):
    all = 0
    for x in n:
        all += x*x
    return all
a = range(1, 2022, 2)
print(sum(a))

