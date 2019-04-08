# Author:karhik J
# Class:Anagram
# Purpose:This class used to find and print the strings are Anagram or not
# Date:08/04/2019
class Anagram:
    def __init__(self):
        print "***Anagram Functionality***"
    def CheckAnagram(self,word1,word2):
        if len(word1)==len(word2):
            if sorted(word1)==sorted(word2):
                return True
        return False
Obj = Anagram()
word1=raw_input("Enter the word1:")
word2=raw_input("Enter the Word2:")
print Obj.CheckAnagram(word1,word2)
