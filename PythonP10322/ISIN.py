# Author:karhik J
# Class:Isin
# Purpose:This class used to find if the string1 presented in the string2
# Date:21/3/19
class Isin:
    CheckString =""
    ContainString =""
    def __init__(self):
        global CheckString
        global ContainString
        CheckString = raw_input("Enter the string need to check")
        ContainString = raw_input("Enter the String which contains the CheckString ")
    def checkStringvalue(self):
        if CheckString.strip() in ContainString.strip():
            return True
        else:
            return False

Isinobj = Isin()
ReturnValue=Isinobj.checkStringvalue()
if ReturnValue:
    print "The value is presented in the given string"
else:
    print "There is no value presented in String"