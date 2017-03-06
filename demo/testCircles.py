import unittest
from CircleADT import *

class CircleTests(unittest.TestCase):
    def setUp(self):
        self.circle = CircleT(2, 2, 2)

    def tearDown(self):
        self.circle = None;
        
    def test_xcoord(self):
        self.assertTrue(self.circle.xcoord() == 2)

    def test_xcoord_returns_other(self):
        self.assertFalse(self.circle.xcoord() == 3)

    def test_intersect_same_circle(self):
        self.assertTrue(self.circle.intersect(self.circle))

    def test_intersect_at_one_point(self):
        circle2 = CircleT(self.circle.xcoord() + self.circle.radius() * 2, self.circle.ycoord(), self.circle.radius())
        self.assertTrue(self.circle.intersect(circle2))

    def test_intersect_at_one_point_away(self):
        circle2 = CircleT(self.circle.xcoord() + self.circle.radius() * 2 + 1, self.circle.ycoord(), self.circle.radius())
        self.assertFalse(self.circle.intersect(circle2))

if __name__ == '__main__':
    unittest.main()
