import tkinter as tk
from tkinter import *

class Guest():
    def __init__(self, rooms, rumsnr):
        self.rooms = rooms
        self.rumsnr = rumsnr
class Room():
    def __init__(self, beds, roomnr, booked):
        self.beds = beds
        self.roomnr = roomnr
        self.booked = False
    
    def bokad(self):
        pass

class Menuprogram():
    def __init__(self, root):
        root.wm_title("Inloggningssida")
        root.minsize(600, 500)
        root.maxsize(600, 500)

        self.topFrame = Frame(root)
        self.topFrame.pack()

        self.bottomFrame = Frame(root)
        self.bottomFrame.pack()

        lbltitle = Label(self.topFrame, text="Välkommen till hotell Transylvanien!", font=("Times", 20, "bold"))
        lbltitle.grid(row=0, column=0, sticky=E)

        btncheck_in = Button(self.bottomFrame, text="Checka in", font=("Times", 15, "bold"), width= 20)
        btncheck_in.grid(row=1, column=0, sticky=E)

        btncheck_out = Button(self.bottomFrame, text="Checka ut", font=("Times", 15, "bold"), width= 20)
        btncheck_out.grid(row=2, column=0, sticky=E)


root = Tk()
Menuprogram(root)
root.mainloop()