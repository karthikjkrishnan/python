# Author:karhik J
# Class:Stringslice
# Purpose:This class used to find the string is palindrome or not
# Date:21/3/
import re
class Stringslice:
    def is_palindrome(self,line):
        temp = line
        if len(line)>0:
            line = line[::-1]
            print "The reverse word",line
        else:
            print "Given string has zero length"
        if temp == line:
            print "The given String",line,"is palindrome"
obj = Stringslice()
inuputWord =raw_input("Enter the input string")
obj.is_palindrome(re.sub('[^A-Za-z0-9]+', '', inuputWord))