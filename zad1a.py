#!/usr/bin/python3

A = [(2, 5), (4, -6), (1, 9)]

print('point  unit  positive')

unit = lambda p: (p[0] ** 2 + p[1] ** 2) <= 1
positive = lambda p: (p[0] > 0) and (p[1] > 0)

for p in A:
    print(p, unit(p), positive(p))

A.sort(key = lambda p: (-p[1], p[0]))
print(A, 'y decreasing, x increasing')

A.sort(key = lambda p: abs(p[0]) + abs(p[1]))
print(A, 'the sum |x|+|y|')


