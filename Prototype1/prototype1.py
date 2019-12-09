#Created by: A.J. Shulman
from tkinter import *
from tkinter import Entry
from tkinter.ttk import Progressbar
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter import simpledialog


#This program is prototype 1. Just the GUI!


data=[100,101,102,103,104,105,106]

root = Tk()
style = ttk.Style()
style.theme_use('default')

#styling
style.configure("orange.horizontal.TEntry", foreground='#ff8f00')
style.configure("orange.TButton", background='#ff8f00', font=("Purisa", 20))
style.configure("orange.Horizontal.TProgressbar", background='#ff8f00')
style.configure("transp.TLabel", font=("Purisa", 20), foreground='black' )
style.configure("norm.TLabel", font=("Purisa", 20), foreground='black', bg='white')

#canvas
c = Canvas(root, background='#8b0000', highlightthickness=3, highlightbackground="black", width=390)
c.grid(row=3,column=1, columnspan=3, pady=3)

y_stretch = 1
y_gap = 20
x_stretch = 0
x_width = 36
x_gap = 20
ctr = 0
for i in range(len(data) - 1 - 10, len(data),1):
	x0 = (ctr) * x_stretch + (ctr) * x_width + x_gap
	y0 = 220 - (data[i] * y_stretch + y_gap)
	x1 = ctr * x_stretch + ctr * x_width + x_width + x_gap
	y1 = 220 - y_gap
	c.create_rectangle(x0-18, y0, x1-18, y1, fill="#ff8f00")
	c.create_text(x0-15, y0, anchor='sw', text=str(int(data[i])), font=("Purisa", 18), fill='white')
	ctr = ctr + 1
	
#progress-bar
bar = Progressbar(length=390, style='orange.Horizontal.TProgressbar')
bar.grid(row=5, column=1, columnspan=3, pady=10, padx=10, sticky=E+W+N+S)
bar['value']=30
#label on progress bar

label=Label(root, text = str(int(bar['value']))+"%", style = 'transp.TLabel')
label.grid(row=5, column=2, pady=10, padx=10, sticky=W)

#Button that submits the weight

weightButton = Button(root, text="Submit Weight", style='orange.TButton')
weightButton.grid(row=2, column=1)

#Type your weight here
weightEntry = Entry(root, width=15,style='orange.horizontal.TEntry',font=("Purisa", 20))
weightEntry.grid(row=1, column=1, padx = 10, pady=10)


#Button that submits the calories

calsButton = Button(root, text="Submit Calories", style='orange.TButton')
calsButton.grid(row=2, column=3)

#Type your cals here
calsEntry = Entry(root, width=15,style='orange.horizontal.TEntry',font=("Purisa", 20))
calsEntry.grid(row=1, column=3, padx=10, pady=10);

funFact=Label(root,text = 'This is the fun fact area! The helpful weight-loss tip will go here!', style = 'norm.TLabel', wraplength=170)
funFact.grid(column=4, row=2, rowspan=4, pady=15, padx=10)

root.mainloop()