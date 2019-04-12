# Author:karhik J
# Class:Coordinate
# Purpose:This class used to represent the coordinate values
# Date:12/04/2019
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def eq(self, a, b):
        return (a == self.x and b == self.y)
    def repr(self):
        print 'Coordinate(', self.getX(), ',', self.getY(), ')'
a = int(raw_input("enter the x coordinate:"))
b = int(raw_input("enter the y coordinate:"))
obj = Coordinate(a, b)
print obj.__str__()
print obj.eq(a, b)
obj.repr()
