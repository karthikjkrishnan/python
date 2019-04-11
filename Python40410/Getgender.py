# Author:karhik J
# Class:Person
# Purpose:This class used to get the gender of the persons
# Date:09/04/2019
class Person:
    def __init__(self):
        pass
    @staticmethod
    def get_gender():
        return "Unknown"
class Male(Person):
    @staticmethod
    def get_gender():
        return "Male"
class Female(Person):
    @staticmethod
    def get_gender():
        return "Female"
Maleobj = Male()
print "Gender:",Maleobj.get_gender()
Femaleobj = Female()
print "Gender:",Femaleobj.get_gender()
