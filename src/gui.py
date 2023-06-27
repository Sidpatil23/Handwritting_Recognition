from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from os import listdir
import numpy as np
import pickle
import cv2
from os import listdir
import cv2

import os
import main




EPOCHS =2
INIT_LR = 1e-3
BS = 32
default_image_size = tuple((224, 224))
image_size = 0

width=256
height=256
depth=3


root = Tk()  # Main window 
f = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
root.title("Handwritten Text Recognition")
root.geometry("1080x720")
root.resizable(0,0)

canvas = Canvas(width=1080, height=250)
canvas.pack()
filename=('banner.png')
load = Image.open(filename)
load = load.resize((1080, 250), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
#photo = PhotoImage(file='landscape.png')
load = Image.open(filename)
img.place(x=1, y=1)
#canvas.create_image(-80, -80, image=img, anchor=NW)

root.configure(background='#FCFCE5')
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)



def click1( ):
	e2.delete("1.0","end-1c")
	filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("jpeg files","*.jpg"),("all files","*.*")) )
	recognized = main.main(filename)
	messagebox.showinfo("Prediction: " + str(recognized[0]))
	e2.insert("1.0",recognized[0])



def clear_all():  # for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()




label1 = Label(root, text="Handwritten Text Recognition")
label1.config(font=('Italic', 18, 'bold'), justify=CENTER, background="silver", fg="red", anchor="center")
label1.pack(fill=X)


frame2.pack_forget()
frame3.pack_forget()


# satisfaction_level = Label(frame2, text="Enter Query Text: ", bg="#FF9A29", fg="Black")
# satisfaction_level.grid(row=1, column=1, padx=10)
e2 = Text(frame2, width=40,height=1)
e2.grid(row=1, column=2,padx=10)





e1 = Text(frame1,height=15, width=70)
e1.grid(row=1, column=2, padx=10,pady=10)



button5 = Button(frame3, text="Browse",command=click1,width=20,height=1)
button5.grid(row=9, column=1, pady=10,padx=10)


frame2.configure(background="silver")
frame2.pack(pady=10)

frame1.configure(background="red")
frame1.pack(pady=10)

frame3.configure(background="silver")
frame3.pack()

# f.configure(background="Submit")
# f.pack()

root.mainloop()
