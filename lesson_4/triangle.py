import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    def area(self):
        half_p = self.perimeter() / 2
        s = math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))
        return s

    def radius_of_circumscribed_circle(self):
        abc = self.a * self.b * self.c
        return abc / (4 * self.area())

    def radius_of_inscribed_circle(self):
        return 2 * self.area() / self.perimeter()

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a != self.b and self.b != self.c and self.a != self.c:
            return "Versatile"
        else:
            return "Isosceles"
