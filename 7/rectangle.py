from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if (x1 >= x2) or (y1 >= y2):
            raise ValueError("Invalid rectangle coordinates")
        
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    def __eq__(self, other):        # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
            raise ValueError("Second argument must be a rectangle")
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        if not isinstance(other, Rectangle):
            raise ValueError("Second argument must be a rectangle")
        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):                 # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

    def intersection(self, other):  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise ValueError("Second argument must be a rectangle")
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other):         # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError("Second argument must be a rectangle")
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):                # zwraca krotkę czterech mniejszych
        center_point = self.center()
        return (Rectangle(self.pt1.x, self.pt1.y, center_point.x, center_point.y),
                Rectangle(center_point.x, self.pt1.y, self.pt2.x, center_point.y),
                Rectangle(self.pt1.x, center_point.y, center_point.x, self.pt2.y),
                Rectangle(center_point.x, center_point.y, self.pt2.x, self.pt2.y))

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

    def test_intersection(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).intersection(Rectangle(2, 3, 4, 5)), Rectangle(2, 3, 3, 4))
        self.assertEqual(Rectangle(0, 0, 4, 4).intersection(Rectangle(2, 2, 6, 6)), Rectangle(2, 2, 4, 4))
        self.assertEqual(Rectangle(0, 0, 10, 10).intersection(Rectangle(2, 2, 4, 4)), Rectangle(2, 2, 4, 4))

    def test_cover(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).cover(Rectangle(2, 3, 4, 5)), Rectangle(1, 2, 4, 5))
        self.assertEqual(Rectangle(1, 1, 2, 2).cover(Rectangle(4, 4, 5, 5)), Rectangle(1, 1, 5, 5))
        self.assertEqual(Rectangle(0, 0, 10, 10).cover(Rectangle(2, 2, 4, 4)), Rectangle(0, 0, 10, 10))
        self.assertEqual(Rectangle(-2, -2, 2, 2).cover(Rectangle(-1, -1, 3, 3)), Rectangle(-2, -2, 3, 3))

    def test_make4(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).make4(), (Rectangle(1, 2, 2, 3), Rectangle(2, 2, 3, 3), Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4)))
        self.assertEqual(Rectangle(0, 0, 2, 2).make4(), (Rectangle(0, 0, 1, 1), Rectangle(1, 0, 2, 1), Rectangle(0, 1, 1, 2), Rectangle(1, 1, 2, 2)))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()