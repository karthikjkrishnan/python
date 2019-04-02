# Author:karhik J
# Class:Stringslice
# Purpose:For Writing Fixed length file into CSV file
# Date:02/04/2019
writefile = open("csvformat.txt","w+")
with open("sample.txt") as readfile:
    for i in readfile:
        line =i
        name = line[0:7]
        age  =line[7:9]
        salary =line[9:17]
        name=name.replace(" ","")
        print name
        age = age.replace(" ","")
        print age
        salary =salary.replace(" ","'")
        print salary
        resultstring = name+","+age+","+salary
        writefile.write(resultstring)
writefile.close()
