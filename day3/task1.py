#Create shapes.py → class Rectangle with area() & perimeter().
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(120, 100)
print(rectangle.area())
print(rectangle.perimeter())

class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
v1 = Cuboid(100, 100, 20)
print(v1.volume())

class Cube:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def volume(self):
        return self.length * self.width * self.height
cube = Cube(100, 100, 100)
print(cube.volume())