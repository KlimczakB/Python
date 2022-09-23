#!/usr/bin/python3

import unittest
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

class TestSets(unittest.TestCase):

    def setUp(self):
        self.v = Vector(1, 2, 3)
        self.w = Vector(2, -3, 2)
        self.S = set([self.v, self.v, self.w])

    def test_Vector(self):
        self.assertNotEqual(self.v, self.w)
        self.assertEqual((self.v + self.w), (Vector(3, -1, 5)))
        self.assertEqual((self.v - self.w), (Vector(-1, 5, 1)))
        self.assertEqual((self.v * self.w), 2)
        self.assertEqual(self.v.cross(self.w), Vector(13, 4, -7))
        self.assertEqual((self.v.length()), (math.sqrt(14)))
        self.assertEqual(len(self.S), 2)
    
    def tearDown(self):
        print("cleaning")
        pass


if __name__ == "__main__":
    unittest.main()
