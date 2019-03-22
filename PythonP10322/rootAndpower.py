# Author:karhik J
# Class:powercalculation
# Purpose:This class used for powercalculation for integer
# Date:21/3/19
class powercalculation:
    integer =0
    def __init__(self):
        global integer
        integer = input("Enter the number")
    def calculatepower(self):
        flag =1
        for root in range(0,integer):
            for power in range(0,6):
                if root**power ==integer:
                    flag=0
                    print "root:",root,"\n","power:",power
                    break
        if flag:
            print "THERE IS NO ROOT AND POWER CALCULATION MATCHED"

obj = powercalculation()
obj.calculatepower()