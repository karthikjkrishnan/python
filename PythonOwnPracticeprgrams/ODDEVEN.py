class oddeven:
    input_number=0
    def __init__(self):
        global input_number
        input_number = raw_input("Enter the Number")
    def oddeven(self):
        global input_number
        input_number =int(input_number)
        if  input_number%2==0:
            if input_number%4==0:
                print "This number is multiples of four and Even number "
            else:
                print "Even"

        else:
            print "odd"
obj=oddeven()
obj.oddeven()
