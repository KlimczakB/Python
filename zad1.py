#!/usr/bin/python3

import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):        # return string "Vector(x, y, z)"
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)

    def __eq__(self, other):   # v == w
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):   # v + w
        # Hint: return Vector(...)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):   # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):  # return the dot product (number)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def cross(self, other):   # return the cross product (Vector)
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z, 
                      self.x * other.y - self.y * other.x)

    def length(self):    # the length of the vector
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)


    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

# Exemplary tests.
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

print('Tests passed')

print('Zadanie 7.1')

def find_axis(v1, v2):
    v3 = v1.cross(v2) #iloczyn wektorowy(cross product)
    if v3 == Vector(0, 0, 0):
        raise ValueError('v1 i v2 są równoległe')
#unit vector = wektor jednostkowy - spełnia zasadę v(wektor)=współrzędne/length(długość)
#jeśli v(0,2,1) to v = v/l =(0,2,1)/sqrt(0^2 + 2^2 + 1^2) 
    l = v3.length()
    v3.x, v3.y, v3.z = v3.x/l, v3.y/l, v3.z/l
    return v3

