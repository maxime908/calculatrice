

class CalculatorBrain:

    def __init__(self):
        self.nb1 = None
        self.nb2 = None
        self.operator = None

    def append(self,value):

        if not value.isdigit() and value not in ["+","-","*"]:
            print("Value must be a digit or an operator")
            return False

        if value.isdigit():
             value = int(value)

        if self.setNb1(value):
            return True
        if self.setOperator(value):
            return True
        if self.setNb2(value):
            return True

        return False

    def setNb1(self, nb1):

        if self.nb1 == None and self.operator == None and self.nb2 == None:
            self.nb1 = nb1
            return True
        
        print("Impossible de set nb1")
        return False
    
    def setNb2(self, nb2):
        if self.nb1 != None and self.operator != None and self.nb2 == None:
            self.nb2 = nb2
            return True
        
        print("Impossible de set nb2")
        return False

    def setOperator(self, op):
        if self.nb1 != None and self.nb2 == None and self.operator == None:
            self.operator = op
            return True
        
        print("Impossible de set operator")
        return False
    
    def reset(self):
        self.nb1 = None
        self.nb2 = None
        self.operator = None
        print("Reset calculator")

    def add(self):
        return self.nb1 + self.nb2
    
    def minus(self):
        return self.nb1 - self.nb2
    
    def time(self):
        return self.nb1 * self.nb2
    
    def doCalculus(self):
        res = None
        if self.operator == "+":
            res = self.add()
        if self.operator == "-":
            res = self.minus()
        if self.operator == "*":
            res = self.time()

        self.reset()
        return res
    
calculator = CalculatorBrain()

calculator.append("%")
calculator.append("+")
calculator.append("2")

res = calculator.doCalculus()
print(res)