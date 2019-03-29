# Author:karhik J
# Class:Newtonsqrt
# Purpose:This class used to find the square root using newtons method and normal math.sqrt method and then finding the difference between two
# Date:29/3/19
import math
class Newtonsqrt:
    inputNumber = 0
    def __init__(self):
        print "****** Difference between newtonsqrt() and math.sqrt()*****"
    def newtonSqrt(self,inputNumber):
        tempValue = inputNumber
        for i in range(20):
            inputNumber = inputNumber - (inputNumber*inputNumber-tempValue)/(2.0*inputNumber)
        return inputNumber
    def Mathsqrt(self,inputNumber):
        return math.sqrt(inputNumber)
def test_square_root (inputNumber):
    newton = obj.newtonSqrt(inputNumber)
    mathsqrt = obj.Mathsqrt(inputNumber)
    difference = abs(newton-mathsqrt)
    print '{:<12}\t{:<12}\t{:<12}\t{:<12}'.format(inputNumber,newton,mathsqrt,difference)

obj = Newtonsqrt()
print '{:<12}\t{:<12}\t{:<12}\t{:<12}'.format('number','newtons', 'libmath', 'difference')
for inputNumber in range(1,10):
    test_square_root(inputNumber)