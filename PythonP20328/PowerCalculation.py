# Author:karhik J
# Class:Powercalculation
# Purpose:This class used for Power calculation
# Date:29/3/19
class Powercalculation:
    def __init__(self):
        print "***power calculation***"
    def Powercalculation(self,number1,number2):
        if number1==1:
            return True
        number3 =number1/number2
        if number1%number2 == 0 and number3/number2 ==1:
            return True
        else:
            return False
number1 = input("Enter the input1")
number2 = input("Enter the input2")
obj = Powercalculation()
power = obj.Powercalculation(number1,number2)
if power:
    print "The given number is powered number"
else:
    print "The given number is not a power number"