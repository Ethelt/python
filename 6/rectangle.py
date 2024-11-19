from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    def __eq__(self, other):        # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):                 # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):            # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self): pass

    def test_str(self): 
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")

    def test_repr(self): 
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")

    def test_eq(self): 
        self.assertTrue(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4))
        self.assertFalse(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 5))

    def test_ne(self): 
        self.assertFalse(Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 4))
        self.assertTrue(Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 5))

    def test_center(self): 
        self.assertEqual(Rectangle(1, 2, 3, 4).center(), Point(2, 3))

    def test_area(self): 
        self.assertEqual(Rectangle(1, 2, 3, 4).area(), 4)

    def test_move(self): 
        rect = Rectangle(1, 2, 3, 4)
        rect.move(1, 1)
        self.assertEqual(rect, Rectangle(2, 3, 4, 5))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()