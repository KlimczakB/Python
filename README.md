# Python

## EXERCISE 6.1

Create 3D vectors as a Python class.
```
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): pass        # return string "Vector(x, y, z)"

    def __eq__(self, other): pass   # v == w

    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other): pass   # v + w
        # Hint: return Vector(...)

    def __sub__(self, other): pass   # v - w

    def __mul__(self, other): pass  # return the dot product (number)

    def cross(self, other): pass   # return the cross product (Vector)

    def length(self): pass   # the length of the vector

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended
```

## Exemplary tests
```
import math
v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
assert v != w
assert v + w == Vector(3, -1, 5)
assert v - w == Vector(-1, 5, 1)
assert v * w == 2
assert v.cross(w) == Vector(13, 4, -7)
assert v.length() == math.sqrt(14)
S = set([v, v, w])
assert len(S) == 2
print("Tests passed")
```
```
two vectors are given (a vector is a 3-tuple here)
a = (a1, a2, a3)
b = (b1, b2, b3)
the dot product (the result is a number)
a_dot_b = a1 * b1 + a2 * b2 + a3 * b3
the cross product (the result is a vector)
a_cross_b = (a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1)
```
