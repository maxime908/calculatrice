import tkinter as tk
from calculatorBrain import CalculatorBrain

class TextField:

    def __init__(self, master, width=10):
        self.maVariable = tk.StringVar()
        tk.Entry(master, width=width, textvariable=self.maVariable).pack()

    def getText(self):
        return self.maVariable.get()

class MyButton:

    def __init__(self, master, text, functionCalled, row, column):
        self.title = text
        self.functionCalled = functionCalled
        tk.Button(master, text=text, anchor="center", relief="flat", foreground="white", background="#ff9500", font=('Verdana', 24, 'bold'), width=5, cursor="target", command=self.on_click).grid(row=row, column=column, padx=5, pady=5, sticky="W")

    def on_click(self):
        print(f"Dans la classe {self.title}")
        self.functionCalled(self)

class MyLabel:
    def __init__(self, master, text):
        tk.Label(master, text=text, anchor="w", wraplength=900, width=40, font=('Verdana', 24, 'bold'), borderwidth=1, relief="solid", padx=10, pady=10).grid(column=0, row=0, columnspan=20, sticky="W")


class MainWindow:

    root = None

    def __init__(self, title, width, height):
        self.root = tk.Tk()
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.resizable(width=False, height=False)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        

    def addButton(self, text, functionCalled, row, column):
        myButton = MyButton(self.root, text, functionCalled, row=row, column=column)
        return myButton
    
    def addLabel(self, text):
        myLabel = MyLabel(self.root, text=text)
        return myLabel

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
        myWindow.addLabel(f"{calculator.total} = {res}")
    else:
        calculator.append(sender.title)

    nb1 = calculator.updateNb1()

    op = calculator.updateOp()

    nb2 = calculator.updateNb2()

    if (op == None):
        op = ""
    
    if (nb2 == None):
        nb2 = ""

    if sender.title != "=":
        myWindow.addLabel(f"{nb1} {op} {nb2}")


calculator = CalculatorBrain()

myWindow = MainWindow("Ma Calculatrice", width=1200, height=800)

titles = [
    {
        "title":"1",
        "row":1,
        "column":2,
    },
    {
        "title":"2",
        "row":1,
        "column":3,
    },
    {
        "title":"3",
        "row":1,
        "column":4,
    },
    {
        "title":"4",
        "row":2,
        "column":2,
    },
    {
        "title":"5",
        "row":2,
        "column":3,
    },
    {
        "title":"6",
        "row":2,
        "column":4,
    },
    {
        "title":"7",
        "row":3,
        "column":2,
    },
    {
        "title":"8",
        "row":3,
        "column":3,
    },
    {
        "title":"9",
        "row":3,
        "column":4,
    },
    {
        "title":"0",
        "row":4,
        "column":3,
    },
    {
        "title":"+",
        "row":1,
        "column":18,
    },
    {
        "title":"-",
        "row":1,
        "column":19,
    },
    {
        "title":"x",
        "row":2,
        "column":18,
    },
    {
        "title":"/",
        "row":2,
        "column":19,
    },
    {
        "title":"=",
        "row":3,
        "column":19,
    },
    ]
for title in titles:
    myButton = myWindow.addButton(title["title"], maFonction, title["row"], title["column"])

label = myWindow.addLabel("")

myWindow.display()