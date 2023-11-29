import tkinter as tk
class Mycalculator:
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("300*300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello DIP01", font=('Arial'))
        self.label.pack()

        self.root.mainloop()

Mycalculator