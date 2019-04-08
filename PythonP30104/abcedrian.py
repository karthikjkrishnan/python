# Author:karhik J
# Class:abcderian
# Purpose:This class used to check if the given word in the alphabetical order or not
# Date:08/04/2019
class abcderian:
    def __init__(self):
        print "******STRING IN ALPHABETICAL ORDER ORDER***********"
    def CheckOrderOftheWord(self,word):
        for i in range(len(word)-1):
            if ord(word[i])>ord(word[i+1]):
                return False
        return True
obj = abcderian()
word= raw_input("Enter the string:")
Result=obj.CheckOrderOftheWord(word)
if Result:
    print "The given word:",word,"is in alphabetical order"
else:
    print "The given word:",word,"is not in alphabetical order"

