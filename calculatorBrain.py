

class CalculatorBrain:

    def __init__(self):
        self.total = None
        self.nb1 = None
        self.nb2 = None
        self.operator = None

    def append(self,value):

        if not value.isdigit() and value not in ["+","-","*","/"]:
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
        
        if self.nb1 != None and self.operator == None and self.nb2 == None and nb1 not in ["+","-","*","/"]:
            var = str(self.nb1) + str(nb1)
            print(var)
            self.nb1 = int(var)
            return True
        
        print("Impossible de set nb1")
        return False
    
    def setNb2(self, nb2):
        if self.nb1 != None and self.operator != None and self.nb2 == None:
            self.nb2 = nb2
            return True
        
        if self.nb1 != None and self.operator != None and self.nb2 != None:
            var = str(self.nb2) + str(nb2)
            print(var)
            self.nb2 = int(var)
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
    
    def divided(self):
        return self.nb1 / self.nb2
    
    def doCalculus(self):
        res = None
        if self.operator == "+":
            res = self.add()
            self.total = f"{self.nb1} {self.operator} {self.nb2}"
        if self.operator == "-":
            res = self.minus()
            self.total = f"{self.nb1} {self.operator} {self.nb2}"
        if self.operator == "!":
            res = self.time()
            self.total = f"{self.nb1} {self.operator} {self.nb2}"
        if self.operator == "/":
            res = self.divided()
            self.total = f"{self.nb1} {self.operator} {self.nb2}"

        self.reset()
        return res