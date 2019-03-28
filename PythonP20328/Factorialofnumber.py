# Author:karhik J
# Class:Isin
# Purpose:This class used to find Factorial of a given number using iterative,recursion ,tail recursion
# Date:21/3/19
class Factorial:
    number = 0
    fact =1
    def __init__(self):
        global number
        number = input("Enter the number to find factorial")
    # Factorial using Iterative method
    def IterativeFactorial(self):
        fact=1
        global number
        while number:
            fact=fact*number
            number = number-1
        print "FACTORAIL USING RECURSION",fact

# Factorial using Recursion method
def Recursivefactorial(n):
            global number
            if n==1:
                return n
            else:
                return n*Recursivefactorial(n-1)
# Factorial using Tail Recursion method
def Tailrecursivefactorial(n,tail=1):
    if n == 0:
        return tail
    else:
        return Tailrecursivefactorial(n - 1,tail*n)



obj = Factorial()
obj.IterativeFactorial()
n = input("Enter the input for recursive factorial")
print "RECURSION FACTORIAL",Recursivefactorial(n)
print "Tail Recursion",Tailrecursivefactorial(n)
