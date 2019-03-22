NormalList=[]
class Listmanipulation:
    ListSize=0

    def __init__(self):
        global ListSize
        ListSize = input("Enter the list size")
    def appendingIntoList(self):
        i=0
        for i in range(ListSize):
            ListItems=raw_input("Enter the list items one by one")
            NormalList.append(int(ListItems))
    def filteringList(self):

        global NormalList
        print "originalList", NormalList
        NormalList=[x for x in NormalList if x<5]
        print "FilteredList",NormalList

obj=Listmanipulation()
obj.appendingIntoList()
obj.filteringList()
