class CustomObject:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return '{}: {}, {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.age)
def keyList(CustomObject):
            return CustomObject.age

CustomobjectList=[CustomObject('karthik',29),CustomObject('venki',25)]
CustomobjectList.sort(key=keyList)
# print("sorted",sorted(CustomobjectList,key=keyList))
print ("CustomObjectList",CustomobjectList)