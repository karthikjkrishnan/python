# Author:karhik J
# Class:Isin
# Purpose:This class used to find GCD VALUE OF TWO NUMBERS
# Date:21/3/19
number1=0
number2=0
class gcd:
    def __init__(self):
        global number1
        global number2
        number1 = input("Enter the number1")
        number2 = input("Enter the number2")
    def gcdValue(self,number1,number2):
        while number2:
            number1, number2 = number2, number1 % number2
        return number1
obj = gcd()
print "GCD VALUE",obj.gcdValue(number1,number2)