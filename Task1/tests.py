import unittest
from math import pi
from shapes import Circle, Triangle, calculate_area


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), pi)
        
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.area(), pi * 2.5**2)
    
    def test_circle_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(ValueError):
            Circle(0)
    
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
        
        triangle = Triangle(3, 3, 3)
        self.assertAlmostEqual(triangle.area(), 3.8971143)
    
    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)
    
    def test_right_angled_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_angled())
        self.assertTrue(Triangle(5, 12, 13).is_right_angled())
        self.assertTrue(Triangle(8, 15, 17).is_right_angled())
        self.assertFalse(Triangle(1, 1, 1).is_right_angled())
    
    def test_calculate_area_polymorphism(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(shape) for shape in shapes]
        self.assertAlmostEqual(areas[0], pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)


if __name__ == "__main__":
    unittest.main()