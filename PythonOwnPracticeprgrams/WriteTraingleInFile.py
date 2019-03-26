# Author:karhik J
# Class:Trainglepattern
# Purpose:This class used to write traingle pattern into the file
# Date:26/3/19
from __future__ import print_function
class Trainglepattern:
    size =0
    type = " "
    def __init__(self):
        global size
        global type
        print("******** Writing the Traingle pattern in file**********")
        size = input("Enter the size of traingle")
    def Triangle(self):
        m=(2*size)-2
        fileopen = open("myfile3.txt", 'a')
        fileopen.truncate()
        for i in range(1,size+1):
            for j in range(0,m):
                fileopen.write(" ")
                print(end=" ")
            m=m-1
            for j in range(i,0,-1):
                fileopen.write("*")
                print("* ", end=' ')
                fileopen.write(" ")
            fileopen.write("\n")
            print(" ")
obj = Trainglepattern()
obj.Triangle()
