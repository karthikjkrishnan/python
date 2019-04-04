# Author:karhik J
# Class:String_of_letters
# Purpose:This class used to find and print the strings which does not contains the given letters
# Date:04/04/2019
class String_of_letters:
    Word = " "
    StringOfLetters=" "
    def __init__(self):
        print "*****Cheking word contains given Letters*****"
        global Word
        global StringOfLetters
        Word = raw_input("Enter the Word")
        StringOfLetters = raw_input("Enter the string of letters")
    def ContainsLetters(self):
        global StringOfLetters
        global Word
        for i in Word:
            if i not in StringOfLetters:
                return False
        return True
    str1=""
    str2=""
    def Wordformation(self,word):
        for i in range(0,len(word)):
            str1=word[4]+word[2]+word[5]+word[5]+word[6]+" "
            str2=word[1]+word[4]+word[2]+word[3]
        print "The Altered String",str1+str2

Sobj = String_of_letters()
value=Sobj.ContainsLetters()
Sobj.Wordformation("acefhlo")
if value:
    print "The given Word only contains the given string of letters"
else:
    print "The given Word cannot contains the given string of letters"