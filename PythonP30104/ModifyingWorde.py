# Author:karhik J
# Purpose:This is used for the finding words and percentage of that words have no 'e'
# Date:04/04/2019
from __future__ import division
li=[]
def eCOunt(word):
        for i in word:
            if i== 'e':
                return True
        return False
flag =0
count= 0
with open("sample.txt","r+") as fobj:
    for line in fobj:
        word=line.split()
        for wordcheck in word:
            flag=flag+1
            if eCOunt(wordcheck)== False:
                count = count+1
                li.append(wordcheck)
    eachWordpercentage = 100 / flag
    print "WORDS DOES NOT CONTAINS E IS ", li
    print "PERNCENTAGE OF THE WORDS", round(count * eachWordpercentage),"%"

