import tkinter as tk
from tkinter import *

roomswithfour = [(4,6),(4,7),(4,8),(4,9),(4,10)]
roomswiththree = [(3,1),(3,2),(3,3),(3,4),(3,5)]

totalRooms = []

class Guest():
    def __init__(self, rooms, rumsnr, ssn):
        self.rooms = rooms
        self.rumsnr = rumsnr
        self.ssn = ssn
class Room():
    def __init__(self, beds, roomnr):
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

        for u in roomswiththree:
            totalRooms.append(Room(*u))
        for i in roomswithfour:
            totalRooms.append(Room(*i))


        self.topFrame = Frame(root)
        self.topFrame.pack()

        self.bottomFrame = Frame(root)
        self.bottomFrame.pack()

        lbltitle = Label(self.topFrame, text="Välkommen till hotell Transylvanien!", font=("Times", 20, "bold"))
        lbltitle.grid(row=0, column=0, sticky=E)

        btncheck_in = Button(self.bottomFrame, text="Checka in", font=("Times", 15, "bold"), width= 25, height= 5)
        btncheck_in.grid(row=1, column=0, sticky=E)

        btncheck_out = Button(self.bottomFrame, text="Checka ut", font=("Times", 15, "bold"), width= 25, height=5)
        btncheck_out.grid(row=2, column=0, sticky=E)

    def checkInButton(self):
        pass



root = Tk()
Menuprogram(root)
root.mainloop()