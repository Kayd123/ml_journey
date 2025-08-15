#Create class Circle with area() & circumference().
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * math.pi * (self.radius * 2)

circle = Circle(7)
print(circle.area())
print(circle.circumference())