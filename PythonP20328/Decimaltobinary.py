# Author:karhik J
# Class:Isin
# Purpose:This class used to convert the binary to decimal
# Date:21/3/19
class decimaltobinary:
    number =0
    def __init__(self):
        global number
        number=input("Enter the number")
    def decimalvalues(self):
        decimal =0
        for i in range(len(str(number))):
                power = len(str(number))-(i+1)
                decimal=decimal+int(str(number)[i])*(2**power)
        print "Decimal value",decimal
obj = decimaltobinary()
obj.decimalvalues()

