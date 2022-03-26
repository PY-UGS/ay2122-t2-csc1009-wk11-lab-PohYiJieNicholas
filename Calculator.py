class Calculator:
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2
        
    def adder(self):
        return self.input1+self.input2

    def subtractor(self):
        return self.input1-self.input2


    def multiplier(self):
        return self.input1*self.input2


    def divider(self):
        return self.input1/self.input2


    def clear(self):
        return 0


print("Enter first input:")
input1 = input()
print("Enter second input:")
input2 = input()

calculator = Calculator(float(input1), float(input2))
print("Addition: ", calculator.adder())
print("Subtraction: ",calculator.subtractor())
print("Multiplication: ",calculator.multiplier())
print("Divide: ",calculator.divider())
print("Clear: ",calculator.clear())

