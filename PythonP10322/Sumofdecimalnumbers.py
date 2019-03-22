# Author:karhik J
# Class:SumofdecimalnumberL
# Purpose:This class used to find the Sum of decimal numbers given in the format of String
# Date:21/3/19
from decimal import Decimal
class Sumofdecimalnumbers:
    DecimalString =" "
    def __init__(self):
        global DecimalString
        DecimalString = raw_input("Enter the String separated by comma(,)")
    def summOfDecimal(self):
        sum=0
        SeparatedString=DecimalString.split(',')
        for i in range(0,len(SeparatedString)):
            sum=sum+Decimal(SeparatedString[i])
        print "SUM OF THE DECIMAL NUMBERS",sum
obj=Sumofdecimalnumbers()
obj.summOfDecimal()

