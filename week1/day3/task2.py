# Create class Circle with area() & circumference().
import math


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)

    def circumference(self) -> float:
        return 2 * math.pi * (self.radius * 2)


circle = Circle(7)
print(circle.area())
print(circle.circumference())
