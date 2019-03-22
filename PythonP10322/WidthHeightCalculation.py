class Widthcalculation:
    width =0
    height =0
    delimeter=0
    def __init__(self):
        global width
        global height
        global delimeter
        width = input("Enter the Width:")
        height = input("Enter the Height:")
        delimeter = raw_input("Enter the delimeter")
    def WidthHeightCalculation(self):
        WidthValue=width/2
        WidthprecisionValue = width/2.0
        heightvalue=height/3
        integervalue=1+2*5
        delimetervalue=delimeter*5
        print "WidthValue:",WidthValue
        print "WidthprecisionValue:", WidthprecisionValue
        print "heightvalue:", heightvalue
        print "integervalue:", integervalue
        print "delimetervalue:", delimetervalue
wobj = Widthcalculation()
wobj.WidthHeightCalculat