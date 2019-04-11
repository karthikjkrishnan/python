# Author:karhik J
# Class:Hashtricks
# Purpose:This class used to print the hashtriks
# Date:11/04/2019
class Hashtricks:
    def __init__(self):
        pass
    def non_recursivemethod(self):
        size=input("Enter the size")
        for i in range(2,size,2):
            s="*"*i
            print s.center(15)
    def recursive(self,value):
        if value==16:
            return
        s="*"*value
        print s.center(15)
        Hashtricks().recursive(value+2)

obj = Hashtricks()
obj.non_recursivemethod()
initial_value = input("Enter the input value")
obj.recursive(initial_value)