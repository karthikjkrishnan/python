# Author:karhik J
# Class:Eval
# Purpose:This class used to apply the eval function and get the solution for the given input value and exit when input is 'done'
# Date:29/3/19
class Eval:
    def __init__(self):
        print "*******Evaluate Function********"
    def eval_loop(self):
        EvalSolution=''
        while True:
            InputValue = raw_input("Enter the input")
            if InputValue.lower() =='done':
                break
            EvalSolution = eval(InputValue)
            print "Solution for the given Expression",EvalSolution
obj = Eval()
obj.eval_loop()

