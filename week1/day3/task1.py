# Create class Rectangle with area() & perimeter().
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return self.width * 2 + self.height * 2


rectangle = Rectangle(120, 100)
print(rectangle.area())
print(rectangle.perimeter())


class Cuboid:
    def __init__(self, length: float, width: float, height: float) -> None:
        self.length: float = length
        self.width: float = width
        self.height: float = height

    def volume(self) -> float:
        return self.length * self.width * self.height


v1 = Cuboid(100, 100, 20)
print(v1.volume())


class Cube:
    def __init__(self, length: float, width: float, height: float) -> None:
        self.length: float = length
        self.width: float = width
        self.height: float = height

    def volume(self) -> float:
        return self.length * self.width * self.height


cube = Cube(100, 100, 100)
print(cube.volume())
