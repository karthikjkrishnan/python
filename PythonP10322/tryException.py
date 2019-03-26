# Author:karhik J
# Class:Dividebyzero
# Purpose:This class used for finding the Raito of two numbers
# Date:21/3/19
list1=[]
list2=[]
list3=[]
class Dividebyzero:
    number1=0
    number2=0
    size =0

    def __init__(self):
        global number1
        global number2
        global size
        print "***********TRY  EXCEPTIONS************"
        size =input("Enter the size")
        for i in range(0,size):
            number1=input("Enter the numbers for list1")
            list1.append(number1)
        for i in range(0,size):
            number1=input("Enter the numbers for list2")
            list2.append(number1)
    def getRatios(self,list1,list2):
        for i,j in zip(list1,list2):
            try:
                list3.append(i/j)
            except Exception, e:
                print "ERROR MESSAGE",str(e)
        print "Final Result",list3

Dividebyzeroobj = Dividebyzero()
Dividebyzeroobj.getRatios(list1,list2)