"""Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of
the shape where Shape's area is 0 by default."""
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length  # Store the side length

    def area(self):
        return self.length ** 2

length = float(input("Enter the length of the square: "))
square = Square(length)

print("Shape area:", Shape().area())
print("Square area:", square.area())
#4 >>> 16.0

