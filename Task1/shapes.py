import math


class Shape():    
    def area(self) -> float:
        pass
    
    def is_right_angled(self) -> bool:
        pass


class Circle(Shape):    
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def is_right_angled(self) -> bool:
        return False


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными числами")
        sides.sort()
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a, self.b, self.c = a, b, c
    
    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def is_right_angled(self) -> bool:
        sides = [self.a, self.b, self.c]
        sides.sort()
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)


def calculate_area(shape: Shape) -> float:
    return shape.area()
