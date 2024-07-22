import pygame as pg
from tkinter import *
import tkinter as tk
from europe_flags import *
from Asia_flags import *
from America_n import *

menu = tk.Tk()
menu.title('Main menu')
menu.minsize(450, 450)
menu.maxsize(450, 450)
menu.config(bg='black')

frame = Frame(menu, bd=0, bg='black')

title = Label(frame, text='Game Mode', bg='black', fg='white', font=45)
title.pack()

button = Button(frame, text='Europe: take and drop flags', command= europe_d)
button.pack()

button = Button(frame, text='Asia: take and drop flags', command=Asia_d)
button.pack()

button = Button(frame, text='S-America: take and drop flags', command=america_n_D)
button.pack()

button = Button(frame, text='N-America: take and drop flags [⛔]')
button.pack()

button = Button(frame, text='Africa: take and drop flags [⛔]')
button.pack()

button = Button(frame, text=': take and drop flags [⛔]')
button.pack()

frame.pack(expand=TRUE)

menu.mainloop()