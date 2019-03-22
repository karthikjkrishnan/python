import datetime
class Hundredyears:
    name=0
    age=0
    def __init__(self):
        global name
        global age
        name=raw_input("Enter the name")
        age=raw_input("Enter the age")
    def AgeCalculation(self):
        global age
        age=100-int(age)
        now=datetime.datetime.now()
        Hundredyear=now.year+age
        print "You celebrate 100th birthday in ",Hundredyear
c=Hundredyears()
c.AgeCalculation()







