#Created by: A.J. Shulman
from tkinter import *
from tkinter import Entry
from tkinter.ttk import Progressbar
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter import simpledialog
import datetime
import random

#VARIABLES*****************
#This list holds the weight
data = []
#This variable stores time
now = datetime.datetime.now()
#This variable stores hour
hour=now.hour
#This variable stores day
day=now.day
#This variable holds the weight data file
rFile = open("data.txt", "r")
#This variable holds the cals data file
rFile2 = open("cals.txt", "r")
#This variable holds the content of the cals data file
cals = float(rFile2.read())
#This variable holds the content of the weight data file
data = rFile.read().split("\n")
#This loop adds each value in the weight data to the data list
for i in range(0, len(data),1):
	data[i] = float(data[i]) #casting

# BELOW CALCULATES THE CALORIC GOAL----------------------------------------

def goalCalsCalc():
	bw=data[len(data)-1]
	heightFile2 = open("height.txt", "r")
	height = float(heightFile2.read())
	ageFile2 = open("age.txt", "r")
	age = float(ageFile2.read())
	mORfFile2 = open("mORf.txt", "r")
	mORf = mORfFile2.read()
	alFile2 = open("al.txt", "r")
	al = int(alFile2.read())

	def mancalc(bw, h, a, al):
		calc1 = (66+(6.3*bw)+(12.9*h)-(6.8*a))
		if al == 1:
			return calc1*1.2
		if al == 2:
			return calc1*1.375
		if al == 3:
			return calc1*1.55
		if al == 4:
			return calc1*1.725
		if al == 5:
			return calc1*1.9
	def wcalc(bw, h, a, al):
		calc1 = (655+(4.3*bw)+(4.7*h)-(4.7*a))
		if al == 1:
			return calc1*1.2
		if al == 2:
			return calc1*1.375
		if al == 3:
			return calc1*1.55
		if al == 4:
			return calc1*1.725
		if al == 5:
			return calc1*1.9

	if mORf=='M'or'm':
		calsGoal=mancalc(bw, height, age, al)
		
	if mORf=='F'or'f':
		calsGoal=wcalc(bw, height, age, al)
	return(calsGoal)


#--FUNCTIONS-----------------------------------------
def dayFunc():
	#This function calls the resetBar() function when it is a new day
	global day
	print(day)
	day2int=0
	dayFile = open("day1.txt", "r")
	day2int = int(dayFile.read())
	print(day2int)  		
	if day!=day2int:
		resetBar()
	dayFile.close()
		
def resetBar():
	#This function resets the bar
	global cals
	cals=0

	
def funFact():
	#This function returns a random fun fact
	r = random.randint(0,5)
	if r==0:
		return 'As with quite literally everything else tied to your physical and mental health, sleep is critical for weight loss.'
	if r==1:
		return 'Weight loss needs to accompany lifestyle changes, otherwise, you’ll too easily shift back into your old patterns and return to your original weight.'
	if r==2:
		return 'Drinking water can boost metabolism by 24–30% over a period of 1–1.5 hours, helping you burn off a few more calories'
	if r==3:
		return 'There are many benefits to eating whole eggs, including helping you lose weight.'
	if r==4:
		return 'Short-term studies suggest intermittent fasting is as effective for weight loss as continuous calorie restriction.'
	if r==5:
		return 'Studies show that sugar (and high-fructose corn syrup) consumption is strongly associated with an increased risk of obesity, as well as conditions including type 2 diabetes and heart disease.'

	
def submitStats():
	#This function writes all the info entered in the first window into their individual .txt files
	with open("height.txt", "w") as myfile:
		myfile.write(str(heightEntry1.get()))
	with open("al.txt", "w") as myfile:
		myfile.write(str(aLEntry1.get()))
	with open("age.txt", "w") as myfile:
		myfile.write(str(ageEntry1.get()))
	with open("data.txt", "a") as myfile:
		myfile.write("\n"+str(weightEntry1.get()))
	with open("mORf.txt", "w") as myfile:
		myfile.write(str(gEntry1.get()))

	root2.destroy()

def weigthRunMe():
	'''This function adds the weight entered into the data list. It will replace the last item in the list if it is the same day and it
	will create a new item if it is the same day.'''
	#Step 2:  Access and then clear widget
	value = weightEntry.get()
	weightEntry.delete(0, 'end')
	#Step 3: Append value to the list
	c.delete("all")
	dayFile = open("day1.txt", "r")
	day2int = int(dayFile.read())		
	if day==day2int:
		data.pop(len(data)-1)
		data.insert(len(data),float(value))	
	elif day!=day2int:
		dayFile2 = open("day1.txt", "w")
		dayFile2.write(str(day))
		dayFile2.close()
		data.append(float(value))
	#Step 4: Update display
	chartUpdate()
	
	
def chartUpdate():
	#This function updates the chart when a new weight is entered.
	#These are local variables only needed inthis function.
	#bar graph
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
#Step 1: Bind this function to an action	

def calsRunMe():
	#This function updates the bar value and label text when calories are entered.
	global cals
	#Step 2:  Access widget
	value1 = float(calsEntry.get())
	
	#Step 3: Add to Variable
	cals+=value1
	#Step 4: Update display	
	bar['value'] = float(cals)/float(calsGoal)*100
	barValue = float(cals)/float(calsGoal)*100
	label['text'] = str(int(round(barValue,0)))+'%'
	calsEntry.delete(0, 'end')


def on_closing():
	#This function saves everything when the second window is closed.
	if messagebox.askokcancel("Save", "Would you like to save everything?"):
		#This is where you write to the file
		wFile = open("data.txt", "w")
		for i in range(0, len(data)-1,1):
			wFile.write(str(data[i])+"\n")
		for i in range(len(data)-1, len(data),1):
			wFile.write(str(data[i]))
		wFile.close()
		wFile2 = open("cals.txt", "w")
		wFile2.write(str(cals))
		dayFile2 = open("day1.txt", "w")
		dayFile2.write(str(day))
		dayFile2.close()
		wFile2.close()
		root.destroy()

#GUI SETUP 2 @@@@@******************************************@@@@@

root2 = Tk()
style2 = ttk.Style()
style2.theme_use('default')
dayFunc()
#styling
style2.configure("2orange.horizontal.TEntry", foreground='#ff8f00')
style2.configure("2orange.TButton", background='#ff8f00', font=("Purisa", 20))
style2.configure("transp.TLabel", font=("Purisa", 20), foreground='black', background='white')
style2.configure("transp1.TLabel", font=("Purisa", 10), foreground='black', background='white')

warning=Label(root2, text='If you have already entered this info, just exit this window and the next window will pop up.', style='transp1.TLabel')
warning.grid(row=1, column=1, padx = 10, pady=10, columnspan=2)


#Age
ageEntry1 = Entry(root2, width=15,style='2orange.horizontal.TEntry',font=("Purisa", 20))
ageEntry1.grid(row=3, column=1, padx = 10, pady=10)

ageEntry1Label=Label(root2, text='Enter Age Here', style='transp.TLabel')
ageEntry1Label.grid(row=2, column=1, padx = 10, pady=10)


#Height
heightEntry1 = Entry(root2, width=15,style='2orange.horizontal.TEntry',font=("Purisa", 20))
heightEntry1.grid(row=3, column=2, padx = 10, pady=10)

heightEntry1Label=Label(root2, text='Enter Height Here (in)', style='transp.TLabel')
heightEntry1Label.grid(row=2, column=2, padx = 10, pady=10)

#Gender
gEntry1 = Entry(root2, width=15,style='2orange.horizontal.TEntry',font=("Purisa", 20))
gEntry1.grid(row=7, column=1, padx = 10, pady=10)

gEntry1Label=Label(root2, text='Male or Female (F or M)?', style='transp.TLabel')
gEntry1Label.grid(row=6, column=1, padx = 10, pady=10)
					
#Activity Level
aLEntry1 = Entry(root2, width=15,style='2orange.horizontal.TEntry',font=("Purisa", 20))
aLEntry1.grid(row=5, column=1, padx = 10, pady=10)

aLEntry1Label=Label(root2, text='Activity Level - 1-5', style='transp.TLabel')
aLEntry1Label.grid(row=4, column=1, padx = 10, pady=10)

#Weight
weightEntry1 = Entry(root2, width=15,style='2orange.horizontal.TEntry',font=("Purisa", 20))
weightEntry1.grid(row=5, column=2, padx = 10, pady=10)

weightEntry1Label=Label(root2, text='Enter Weight Here (lbs.)', style='transp.TLabel')
weightEntry1Label.grid(row=4, column=2, padx = 10, pady=10)

#Button for Submition
submit1 = Button(root2, text="Submit", style='2orange.TButton', command=submitStats)
submit1.grid(row=6, column=2, padx = 10, pady=10, rowspan=2, ipady=20, ipadx=20)

root2.mainloop()

calsGoal = goalCalsCalc()

#GUI SETUP ROOT1 ********************************************************************
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

#progress-bar
bar = Progressbar(length=390, style='orange.Horizontal.TProgressbar')
bar.grid(row=5, column=1, columnspan=3, pady=10, padx=10, sticky=E+W+N+S)
bar['value']=cals/calsGoal*100
#label on progress bar

label=Label(root, text = str(int(bar['value']))+"%", style = 'transp.TLabel')
label.grid(row=5, column=2, pady=10, padx=10, sticky=W)

chartUpdate();

#Button that submits the weight

weightButton = Button(root, text="Submit Weight", style='orange.TButton', command = weigthRunMe)
weightButton.grid(row=2, column=1)

#Type your weight here
weightEntry = Entry(root, width=15,style='orange.horizontal.TEntry',font=("Purisa", 20))
weightEntry.grid(row=1, column=1, padx = 10, pady=10)


#Button that submits the calories

calsButton = Button(root, text="Submit Calories", style='orange.TButton', command = calsRunMe)
calsButton.grid(row=2, column=3)

#Type your cals here
calsEntry = Entry(root, width=15,style='orange.horizontal.TEntry',font=("Purisa", 20))
calsEntry.grid(row=1, column=3, padx=10, pady=10);

funFact=Label(root,text = funFact(), style = 'norm.TLabel', wraplength=170)
funFact.grid(column=4, row=2, rowspan=4, pady=15, padx=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()