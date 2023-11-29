import tkinter as tk
class Mycalculator:
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("300*300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello DIP01", font=('Arial',18))
        self.label.pack()

        self.button = tk.Button(self.root, text="c", height=4)
        self.button.place(x=30,y=50)

        self.button = tk.Button(self.root, text="()", height=4)
        self.button.place(x=110,y=50)

        self.button = tk.Button(self.root, text="%", height=4)
        self.button.place(x=190,y=50)

        self.button = tk.Button(self.root, text="/", height=4)
        self.button.place(x=270,y=50)

        self.button = tk.Button(self.root, text="7", height=4)
        self.button.place(x=30,y=70)

        self.button = tk.Button(self.root, text="8", height=4)
        self.button.place(x=110,y=70)

        self.button = tk.Button(self.root, text="9", height=4)
        self.button.place(x=190,y=70)

        self.button = tk.Button(self.root, text="10", height=4)
        self.button.place(x=280,y=70)

        self.button = tk.Button(self.root, text="11", height=4)
        self.button.place(x=200,y=50)

        self.button = tk.Button(self.root, text="12", height=4)
        self.button.place(x=200,y=50)

        self.root.mainloop()

Mycalculator()