# Author:karhik J
# Class:Isin
# Purpose:This class used to find Sumofdigits of a given value
# Date:21/3/19
class Sumofdigits:
    value =""
    def __init__(self):
        global value
        value = raw_input("Enter the value")
    def Sumofdigits(self):
        Sum = 0
        for i in value:
            try:
                Sum = Sum+int(i)
            except ValueError as e:
                print str(e)
        print "SUM OF DIGITS",Sum
obj = Sumofdigits()
obj.Sumofdigits()

