class Fibonacci:

    def __init__(self):
        print("FibonnaciSeries")

    def CalculateFibonnaciValue(self,fibonacciNumber):
        self.Initialvalue = 0
        self.NextValue = 1
        count = 0
        while count<fibonacciNumber:
            self.FibonacciValue = self.Initialvalue+self.NextValue
            self.Initialvalue = self.NextValue
            self.NextValue = self.FibonacciValue
            print (self.FibonacciValue)
            count +=1

ref = Fibonacci()
InputNumber = input("Enter the inputNumber To check Fibonacci")
ref.CalculateFibonnaciValue(InputNumber)