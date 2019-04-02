# Author:karhik J
# Class:Stringslice
# Purpose:This class used to Rotate the given string based on the shift value
# Date:02/04/2019
class Rotateword:
    def rotateString(self,word,shift):
        rotated_string = ''
        leftbound=ord('a')
        rightbound=ord('z')
        for letter in word:
            order_value=ord(letter)+shift
            while order_value >rightbound:
                order_value = order_value-26
            while order_value<leftbound:
                order_value = order_value+26
            converted = chr(order_value)
            rotated_string = rotated_string+converted
        return rotated_string
obj = Rotateword()
word = raw_input("Enter the string want to rotate")
shift = input("Enter the shift")
Rotate_Word=obj.rotateString(word,shift)
print "RotateWord",Rotate_Word
