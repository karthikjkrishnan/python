# Author:karhik J
# Class:Listorder
# Purpose:This class used to check the given list is in ascending order or not
# Date:08/04/2019
class Listorder:
    def __init__(self):
        print "CHECKING LIST IS IN ASCENDING ORDER OR NOT"
    def ListOrder(self,takenList):
        for i in range(len(takenList)-1):
            if takenList[i]>takenList[i+1]:
                return False
        return True
Obj=Listorder()
List1=[]
ListSize = input("Enter the List size")
for i in range(0,ListSize):
    inputList = raw_input("Enter the List items")
    try:
        List1.append(int(inputList))
    except:
        List1.append(inputList)
print List1
value = Obj.ListOrder(List1)
if value:
    print "The given list in the Ascending order"
else:
    print "The given List is not in ascending order"

