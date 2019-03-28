# Author:karhik J
# Class:Isin
# Purpose:This class used to find First even number in the given list
# Date:21/3/19
list1 = []
class Even:
    def __init__(self):
        size = input("Enter the size")
        print "Enter the",size,"numbers"
        for i in range(0,size):
            Inputnumbers=input()
            list1.append(Inputnumbers)
    def checkEven(self,list1):
        for i in list1:
                if i%2==0:
                    return i
        raise ValueError ("There is no even numbers in the given list")

obj = Even()
print "First Even number in teh given list",obj.checkEven(list1)

