#!/usr/bin/python3

from tkinter import *
import random

root = Tk()
root.geometry('200x100')
root.title('DICE')

def roll():
    a = random.choice(['1','2','3','4','5','6'])
    label.configure(text=a)
    

label = Label(root, text='', width=8, height=2, bg='white')
label.pack(side=TOP)

frame = Frame(root, relief=RAISED, bd=5)
frame.pack()

button = Button(frame, bg='orange', text='Roll', relief=RAISED, bd=5, command=roll)
button.pack(side=BOTTOM)

root.mainloop()
