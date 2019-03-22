# Author:karhik J
# Class:Interpretorcalculation
# Purpose:This class used to calculate some basic operations
# Date:21/3/19
from __future__ import division
class Interpretorcalculation:
    r=0
    def __init__(self):
        global r
        print "***********INTERPRETOR CALCULATION*****************"
        r=input("Enter the radius")
    def sphereVolume(self):
        volume = 4/3*3.14*(r*r*r)
        print "volume of sphere",volume
    def Bookcalculation(self):
        Coverprice=24.95
        Discount =(Coverprice/100)*40
        Actualprice = Coverprice-Discount
        total = 0
        intialActualprice=0
        totalActualprice=0
        for i in range(0,60):

            if i == 0:
                intialActualprice = Actualprice+3
            else:
                totalActualprice=totalActualprice+Actualprice+0.75
        print "TotalPrice:",totalActualprice+intialActualprice
    def timeCalculation(self):
        Leavingtime=6+52/60.0
        Easypacetime = (8+15/60)/60
        Tempopacetime = (7+12/60)/60
        Spendtime = 2*Easypacetime+3*Tempopacetime
        Actualtime =Spendtime+Leavingtime
        Stringtime = str(Actualtime)
        Breakfatstime=Stringtime.split('.')
        print "BREAK FAST TIME ",Breakfatstime[0],':',Breakfatstime[1]


obj = Interpretorcalculation()
obj.sphereVolume()
obj.Bookcalculation()
obj.timeCalculation()