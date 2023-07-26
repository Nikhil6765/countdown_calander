from tkinter import Tk, Canvas
from datetime import date, datetime

# creating the canvas

root=Tk()  # creating a tkinter window

c=Canvas(root, width=800, height=800, bd='black')  # canvas of 800 by 800 created

c.pack()  # packs the canvas into tkinter window

c.create_text(100,50,anchor='w',fill='orange',font='Arial 28 bold underline', text='My Countdown Calander')
