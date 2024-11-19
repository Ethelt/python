class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):             # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):        # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):       # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test__str__(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(str(Point(-1, -2)), "(-1, -2)")

    def test__repr__(self):
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")
        self.assertEqual(repr(Point(-1, -2)), "Point(-1, -2)")

    def test__eq__(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(-1, -2))

    def test__ne__(self):
        self.assertFalse(Point(1, 2) != Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(-1, -2))

    def test__add__(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))
        self.assertEqual(Point(-1, -2) + Point(-3, -4), Point(-4, -6))  

    def test__sub__(self):
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))
        self.assertEqual(Point(-1, -2) - Point(-3, -4), Point(2, 2))

    def test__mul__(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)
        self.assertEqual(Point(-1, -2) * Point(-3, -4), 11)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)
        self.assertEqual(Point(-1, -2).cross(Point(-3, -4)), -2)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(-3, -4).length(), 5)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash((1, 2)))
        self.assertEqual(hash(Point(-1, -2)), hash((-1, -2)))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()