# Author:karhik J
# Class:Jusify
# Purpose:This class used to Justify the given value
# Date:20/3/19
class Jusify:
    def __init__(self):
        global name
        print("RIGHT JUSTIFICATION")
    def right_justify(self,name):
        print "%70s"%name
justifyobj = Jusify()
name=raw_input("ENTER THE STRING TO JUSTIFY")
justifyobj.right_justify(name)