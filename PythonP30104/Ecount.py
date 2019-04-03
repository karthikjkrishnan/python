# Author:karhik J
# Class:Ecount
# Purpose:This class used to find the given word contains the e or not
# Date:03/04/2019
class Ecount:
    def __init__(self):
        print "***E WORD COUNT***"
    def eCOunt(self):
        with open("sample.txt","r+") as fobj:
            for line in fobj:
                word=line.split()
                print word
                for i in word:
                    for letter in i:
                        print letter
                        if letter == 'e':
                            return True

fobj = Ecount()
value=fobj.eCOunt()
print value
if value == True:
    print "The file contains the e letter"
else:
    print "The letter does not contains the e letter"