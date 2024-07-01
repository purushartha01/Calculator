# Basic CLI based Calculator


class Calculator:
    def __init__(self):
        self.availableOperations = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
        ]

    def getOperations(self):
        return self.availableOperations

    def Addition(self, a, b):
        return a + b

    def Subtraction(self, a, b):
        return a - b

    def Multiplication(self, a, b):
        return a * b

    def Division(self, a, b):
        return a / b


if __name__ == "__main__":

    Calculator = Calculator()

    while True:
        print("\n\n")
        print("CLI based Calculator:\n\n")
        print("Available Operations: \n")
        print("Addition")
        print("Subtraction")
        print("Mutliplication")
        print("Division")
        print("Exit\n\n")


        op = str(input("Choose an Operation: "))
        if(op not in Calculator.getOperations()):
            break

        var1=int(input("Enter 1st operand: "))
        var2=int(input("Enter 2nd operand: "))
        
        performOp={"Addition":Calculator.Addition,"Subtraction":Calculator.Subtraction,"Multiplication":Calculator.Multiplication,"Division":Calculator.Division}
        print("\n\nResult: ",performOp[op](var1,var2))