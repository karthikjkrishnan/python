# Author:karhik J
# Class:Monetary
# Purpose:This class used to convert the currency type
# Date:09/04/2019
class Monetary:
    def __init__(self,dollar,cent):
        self.dollar=dollar
        self.cent=cent
    def repr(self):
        if int(self.cent)<=99:
            self.displaymoney =(self.dollar,self.cent)
            self.monetary =".".join(self.displaymoney)
            print "The currency is $:",self.monetary
        else:
            self.normalized = float(self.cent)/100
            self.monetary = float(self.dollar)+self.normalized
            print "The currency is $:", self.monetary
        self.add()
        raw_text = u"\u20B9"
        print "EQUAL INDIAN",u"\u20B9",":",self.indian_rupee
        print "EQUAL CHINESE YUAN ",u"\uFFE5",":", self.china_rupee
        print "EQUAL AUSTRALIA DOLLAR A$", self.australia_rupee
    def add(self):
        self.indian_rupee = float(self.monetary)*69.52
        self.china_rupee = float(self.monetary)*6.71
        self.australia_rupee = float(self.monetary)*1.40
    def getrs(self):
        return self.indian_rupee
    def getyuan(self):
        return self.china_rupee
    def getpesos(self):
        return self.australia_rupee


dollar = raw_input("Enter the dollars")
cent = raw_input("Enter the cent")
obj=Monetary(dollar,cent)
obj.repr()