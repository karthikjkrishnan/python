# Author:karhik J
# Class:Shape
# Purpose:This class used to get the area of the square
# Date:09/04/2019
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length

Squareobj = Square(2)
print "Area of the square",Squareobj.area()