# Author:karhik J
# Class:oddNumberofThree
# Purpose:This class used to find the maximum odd value in the given three values
# Date:20/3/19
class oddNumberofThree:
    def __init__(self):
        print "*******ODD OFF THREE*********"
        global x
        global y
        global z
        x = input("ENTER THE FIRST NUMBER")
        y = input("ENTER THE SECOND NUMBER")
        z = input("ENTER THE THIRD NUMBER")
    def checkOdd(self):
        large=0
        if x%2==1:
            large = x
        if y%2 ==1:
            if y>large:
                large = y
        if z%2==1:
            if z>large:
                large = z
        if large:
            print "Largest of numers",large
        else:
            print "THERE ID NO ODD NUMBERS"


obj = oddNumberofThree()
obj.checkOdd()


