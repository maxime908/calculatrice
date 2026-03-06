import tkinter as tk
from calculatorBrain import CalculatorBrain

class TextField:

    def __init__(self, master, width=10):
        self.maVariable = tk.StringVar()
        tk.Entry(master, width=width, textvariable=self.maVariable).pack()

    def getText(self):
        return self.maVariable.get()
    
class MyButton:

    def __init__(self, master, text, functionCalled):
        self.title = text
        self.functionCalled = functionCalled
        tk.Button(master, text=text, command=self.on_click).pack()

    def on_click(self):
        print(f"Dans la classe {self.title}")
        self.functionCalled(self)
    

class MainWindow:

    root = None

    def __init__(self, title, width=300, height=600):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
    
    def addButton(self, text, functionCalled):
        myButton = MyButton(self.root, text, functionCalled)
        return myButton

    def addEntry(self):
        monSuperTextField = TextField(self.root, width=20)
        return monSuperTextField

    def display(self):
        # start the main event loop
        self.root.mainloop()

def maFonction(sender):
    print(f"J'ai été clické par {sender.title}")

    if sender.title == "=":
        res = calculator.doCalculus()
        print(res)
    else:
        calculator.append(sender.title)


calculator = CalculatorBrain()

myWindow = MainWindow("Ma Calculatrice", width=800)
titles = ["1","2","3","+","-","="]
for title in titles:
    myButton = myWindow.addButton(title, maFonction)

myWindow.display()