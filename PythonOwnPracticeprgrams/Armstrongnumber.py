class ArmstrongNumber:

    def __init__(self):
        print("*************ARMSTRONG NUMBER PROGRAM***************")
    def __chechArmstrongNumber__(self,input_Number):
        self.original_Number = input_Number
        resultedNumber=0
        while self.original_Number!=0:
            remainderNumber = self.original_Number%10
            resultedNumber+=remainderNumber*remainderNumber*remainderNumber
            self.original_Number = self.original_Number/10
        if resultedNumber == input_Number:
            print ("ArmstrongNumber")
        else:
            print("Not An ArmstrongNumber")

obj=ArmstrongNumber()
Number = input("Enter the Input Number To Check Armstrong Property")
obj.__chechArmstrongNumber__(Number)

