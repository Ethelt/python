from rectangle import Rectangle, Point
import pytest

def test_from_points():
    assert Rectangle.from_points((Point(1, 2), Point(3, 4))) == Rectangle(1, 2, 3, 4)

def test_str():
    assert str(Rectangle(1, 2, 3, 4)) == "[(1, 2), (3, 4)]"

def test_repr():
    assert repr(Rectangle(1, 2, 3, 4)) == "Rectangle(1, 2, 3, 4)"

def test_eq():
    assert Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4)
    assert not Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 5)

def test_ne():
    assert not Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 4)
    assert Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 5)

def test_center():
    assert Rectangle(1, 2, 3, 4).center() == Point(2, 3)

def test_area():
    assert Rectangle(1, 2, 3, 4).area() == 4

def test_move():
    rect = Rectangle(1, 2, 3, 4)
    rect.move(1, 1)
    assert rect == Rectangle(2, 3, 4, 5)

def test_intersection():
    assert Rectangle(1, 2, 3, 4).intersection(Rectangle(2, 3, 4, 5)) == Rectangle(2, 3, 3, 4)
    assert Rectangle(0, 0, 4, 4).intersection(Rectangle(2, 2, 6, 6)) == Rectangle(2, 2, 4, 4)
    assert Rectangle(0, 0, 10, 10).intersection(Rectangle(2, 2, 4, 4)) == Rectangle(2, 2, 4, 4)

def test_cover():
    assert Rectangle(1, 2, 3, 4).cover(Rectangle(2, 3, 4, 5)) == Rectangle(1, 2, 4, 5)
    assert Rectangle(1, 1, 2, 2).cover(Rectangle(4, 4, 5, 5)) == Rectangle(1, 1, 5, 5)
    assert Rectangle(0, 0, 10, 10).cover(Rectangle(2, 2, 4, 4)) == Rectangle(0, 0, 10, 10)
    assert Rectangle(-2, -2, 2, 2).cover(Rectangle(-1, -1, 3, 3)) == Rectangle(-2, -2, 3, 3)

def test_make4():
    assert Rectangle(1, 2, 3, 4).make4() == (Rectangle(1, 2, 2, 3), Rectangle(2, 2, 3, 3), Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4))
    assert Rectangle(0, 0, 2, 2).make4() == (Rectangle(0, 0, 1, 1), Rectangle(1, 0, 2, 1), Rectangle(0, 1, 1, 2), Rectangle(1, 1, 2, 2))

def test_properties():
    assert Rectangle(1, 2, 3, 4).width == 2
    assert Rectangle(1, 2, 3, 4).height == 2
    assert Rectangle(1, 2, 3, 4).top == 2
    assert Rectangle(1, 2, 3, 4).left == 1
    assert Rectangle(1, 2, 3, 4).bottom == 4
    assert Rectangle(1, 2, 3, 4).right == 3
    assert Rectangle(1, 2, 3, 4).topleft == Point(1, 2)
    assert Rectangle(1, 2, 3, 4).topright == Point(3, 2)
    assert Rectangle(1, 2, 3, 4).bottomright == Point(3, 4)
    assert Rectangle(1, 2, 3, 4).bottomleft == Point(1, 4)