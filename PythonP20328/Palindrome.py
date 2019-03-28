# Author:karhik J
# Class:Isin
# Purpose:This class used to find the string is palindrome or not
# Date:21/3/19
import re
str1=""
class Palindrome:
    def __init__(self):
        print "*************PALINDROME OR NOT*******************"
    def CheckPalindrome(self,str1):
        str2= " "
        str1 = re.sub('[^ a-zA-Z0-9]', '', str1)
        print str1
        for i in str1:
            str2 = i + str2
        checkvalue = str1 in str2
        if(checkvalue==True):
            return True


obj = Palindrome()
str1 = raw_input("Enter the input string")
check=obj.CheckPalindrome(str1)
if check == True:
    print re.sub('[^ a-zA-Z0-9]', '', str1),"palindrome"


