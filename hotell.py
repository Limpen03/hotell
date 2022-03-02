import tkinter as tk
from tkinter import *

class Main():
    def __init__(self, root):
        root.wm_title("Inloggningssida")
        root.minsize(500, 500)

        self.topFrame = Frame(root)
        self.topFrame.pack()

        bottomFrame = Frame(root)
        bottomFrame.pack()

        lbltitle = Label(self.topFrame, text="Välkommen till Scandic hotell!", font=("Arial", 25))
        lbltitle.grid(row=0, column=0, sticky=E)



root = Tk()
Main(root )
root.mainloop()