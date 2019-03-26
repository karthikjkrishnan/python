# Author:karhik J
# Class:Occurencesoftheword
# Purpose:This class used to find the Occurences of the word in the file
# Date:26/3/19
class Occurencesoftheword:
    FileName = ''
    SearchWord = ''
    def __init__(self):
        global FileName
        global SearchWord
        print "*******Occurences Of the Word in file**********"
        FileName = raw_input("Enter the file Name")
        SearchWord = raw_input("Enter the word to search")
    def Occurence(self):
        CountofWord = 0
        with open(FileName,'r') as fileobject:
            for line in fileobject:
                words=line.split()
                for word in words:
                    if(SearchWord==word):
                        CountofWord =CountofWord+1
        print "Ocurences of the Word"
        print CountofWord
obj = Occurencesoftheword()
obj.Occurence()


