'''Define a class named Shape and its subclass Square. The Square
class has an init function which takes length as argument. Both
classes have an area function which can print the area of the
shape where Shape’s area is 0 by default.'''
class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
            return self.length**2
shape=shape()
square=square(7)
print(shape.area())
print(square.area())