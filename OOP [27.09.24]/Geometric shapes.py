from math import pi


class Figure:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses")
    
    def perimeter(self):
        raise NotImplementedError("This method should be overridden in subclasses")


class TwoDimensionalFigure(Figure):
    def __init__(self):
        super().__init__()

    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()


class ThreeDimensionalFigure(Figure):
    def __init__(self):
        super().__init__()

    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()


class Circle(TwoDimensionalFigure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(TwoDimensionalFigure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Sphere(ThreeDimensionalFigure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 4 * pi * self.radius ** 2


class Cube(ThreeDimensionalFigure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return 6 * self.side ** 2

    def perimeter(self):
        return 12 * self.side

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
sphere = Sphere(radius=3)
cube = Cube(side=5)

print(f'The area of the circle: {round(circle.area())}')
print(f'The perimeter of the circle: {round(circle.perimeter())}')
print('--------------------------------------------------------')
print(f'The area of the rectangle: {rectangle.area()}')
print(f'The perimeter of the rectangle: {rectangle.perimeter()}')
print('--------------------------------------------------------')
print(f'The area of the sphere: {round(sphere.area())}')
print('--------------------------------------------------------')
print(f'The area of the cube: {cube.area()}')
print(f'The perimeter of the cube: {cube.perimeter()}')