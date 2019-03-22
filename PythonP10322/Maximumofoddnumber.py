# Author:karhik J
# Class:Oddnumber
# Purpose:This class used to find the maximum odd value in the set of values
# Date:21/3/19
Arrayvalues=[]
class Oddnumber:
    large=0
    def __init__(self):
        print("***********MAXIMUM ODD VALUE IN ARRAY OF VALUES****************")
        Sizeofarray = input("Enter the size input")
        for i in range(0,Sizeofarray):
            InputValues = input("Enter the input elements")
            Arrayvalues.append(InputValues)

    def findMaximumValue(self):
        large =0
        for i in Arrayvalues:
            if i%2==1:
                large=i
        if large:
            print "LARGEST ODD NUMBER IN THE GIVEN ARRAY", large
        else:
            print "THERE IS NO ODD NUMBERS IN THE GIVEN ARRAY"

obj = Oddnumber()
obj.findMaximumValue()