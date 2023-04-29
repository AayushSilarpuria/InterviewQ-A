# Inheritance Example
class Shape:
    def __init__(self, length):
        self.length = length

    def show(self):
        print(f'The lenght is {self.length}')


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def areaOfSquare(self):
        print(f'Area of Square is {self.length**2}.')


class Triangle(Shape):
    def __init__(self, height, length):
        self.length = length
        self.height = height

    def areaOfTriangle(self):
        print(f"Area of Traingle is {(self.length*self.height)/2}")


shape_obj = Shape(5)
shape_obj.show()

square_obj = Square(8)
square_obj.show()
square_obj.areaOfSquare()

traingle_obj = Triangle(12, 5)
traingle_obj.show()
traingle_obj.areaOfTriangle()
