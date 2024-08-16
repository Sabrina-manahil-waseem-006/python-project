
from tkinter import *
import pyodbc
def close():
	m.destroy()

m = Tk()
width = 1500
height = 750
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()

x_coordinate = (screen_width - width) // 2
y_coordinate = (screen_height - height) // 2

m.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')
m.title('Welcome page')
m.overrideredirect(1)
m.resizable(False, False)

fimage = PhotoImage(file="E:\\welcome1.png")
x = Label(m, image=fimage)
x.pack()

logo = Label(m, text="  WELCOME TO LEARN PLAY ZONE   ", font="cambria 32 bold", bg="cadet blue",foreground='gray10', borderwidth=15, relief="groove")
logo.place(relx=0.5, rely=0.45, anchor='center')

play_button = Button(m, text="LET'S PLAY", bg="DARKORANGE1", foreground='BLACK', font="cambria 19 bold", borderwidth=5, relief=SOLID, command=close)
play_button.place(relx=0.5, rely=0.7, anchor='center')

m.mainloop()

def score():
	con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
						 r'DBQ=C:\Users\user\Documents\Database4.accdb;')
	cr1 = con.cursor()

	# Insert data into the 'score' table
	cr1.execute(f"INSERT INTO score (marks) VALUES ({p})")
	con.commit()

	# Retrieve data from the 'score' table
	cr1.execute("SELECT TOP 1 marks FROM score ORDER BY id DESC")
	row = cr1.fetchone()
	con.close()
	lab = Label(c,text =f"YOU HAVE SCORED {row} ",font="arialblack 15 bold",bg="green",padx=70,pady=4)
	lab.place(x=600,y=500)

def swing():
	c1 = Canvas(r, width=580, height=80)
	c1.place(x=580, y=600)
	c1.create_rectangle(1, 1, 580, 580, fill="skyblue1")
	ll = Label(c1, text="YOU HAVE REACHED THE END!", font="arialblack 21 bold", bg="skyblue1")
	ll.place(x=70, y=20)
	L5 = Label(c, text="_______________", font=" calibri 10", bg="deepskyblue4", padx=148, pady=9)
	L5.place(x=600, y=500)
	img = PhotoImage(file="E:\\swing.png")
	img2 = img.subsample(2, 2)
	limg2 = Label(c, image=img2, borderwidth=5, relief='raised')
	limg2.image = img2  # Keep a reference to the image to prevent it from being garbage collected
	limg2.place(x=200, y=250)

	ch1 = Radiobutton(c, text="SLIDE", font="arialblack 19 bold", bg="lightgreen", padx=62, variable=selected_option,
					  value=21,
					  command=wrong)
	ch2 = Radiobutton(c, text="CYCLE", font="arialblack 19 bold", bg="lightblue", padx=58, variable=selected_option,
					  value=22, command=wrong)
	ch3 = Radiobutton(c, text="SEESAW", font="arialblack 19 bold", bg="yellow", padx=58, variable=selected_option,
					  value=23, command=wrong)
	ch4 = Radiobutton(c, text="SWING", font="arialblack 19 bold", bg="darkorange", padx=69,
					  variable=selected_option, value=24, command=correct)

	ch1.place(x=500, y=300)
	ch2.place(x=500, y=400)
	ch3.place(x=800, y=300)
	ch4.place(x=800, y=400)

	b1 = Button(c, text="VIEW SCORE", bg="gray", font="arialblack 19 bold", command=score)
	b1.place(x=700, y=540)


def icecream():
	L5 = Label(c, text="_______________", font=" calibri 10", bg="deepskyblue4", padx=148, pady=9)
	L5.place(x=600, y=500)
	img = PhotoImage(file="E:\\icecream.png")
	img2 = img.subsample(2, 2)
	limg2 = Label(c, image=img2, borderwidth=5, relief='raised')
	limg2.image = img2  # Keep a reference to the image to prevent it from being garbage collected
	limg2.place(x=200, y=250)

	ch1 = Radiobutton(c, text="LOLLIPOP", font="arialblack 19 bold", bg="lightblue", padx=37, variable=selected_option,
					  value=17,
					  command=wrong)
	ch2 = Radiobutton(c, text="CANDY", font="arialblack 19 bold", bg="darkorange", padx=57, variable=selected_option,
					  value=18, command=wrong)
	ch3 = Radiobutton(c, text="ICE CREAM", font="arialblack 19 bold", bg="lavender", padx=39, variable=selected_option,
					  value=19, command=correct)
	ch4 = Radiobutton(c, text="CAKE", font="arialblack 19 bold", bg="lightgreen", padx=76,
					  variable=selected_option, value=20, command=wrong)

	ch1.place(x=500, y=300)
	ch2.place(x=500, y=400)
	ch3.place(x=800, y=300)
	ch4.place(x=800, y=400)

	b1 = Button(c, text="NEXT >>>", bg="gray", font="arialblack 19 bold", command=swing)
	b1.place(x=900, y=600)
	b1 = Button(c, text="<<< PREVIOUS", bg="gray", font="arialblack 19 bold", command=ball)
	b1.place(x=600, y=600)


def ball():
	L5 = Label(c, text="_______________", font=" calibri 10", bg="deepskyblue4", padx=148, pady=9)
	L5.place(x=600, y=500)
	img = PhotoImage(file="E:\\bally.png")
	img2 = img.subsample(2, 2)
	limg2 = Label(c, image=img2, borderwidth=5, relief='raised')
	limg2.image = img2  # Keep a reference to the image to prevent it from being garbage collected
	limg2.place(x=200, y=250)

	ch1 = Radiobutton(c, text="BALL", font="arialblack 19 bold", bg="darkorange", padx=66, variable=selected_option,
					  value=13,
					  command=correct)
	ch2 = Radiobutton(c, text="BAT", font="arialblack 19 bold", bg="lightblue", padx=76, variable=selected_option,
					  value=14, command=wrong)
	ch3 = Radiobutton(c, text="HOCKEY", font="arialblack 19 bold", bg="lightgreen", padx=56, variable=selected_option,
					  value=15, command=wrong)
	ch4 = Radiobutton(c, text="RACKET", font="arialblack 19 bold", bg="brown", padx=59,
					  variable=selected_option, value=16, command=wrong)

	ch1.place(x=500, y=300)
	ch2.place(x=500, y=400)
	ch3.place(x=800, y=300)
	ch4.place(x=800, y=400)

	b1 = Button(c, text="NEXT >>>", bg="gray", font="arialblack 19 bold", command=icecream)
	b1.place(x=900, y=600)
	b1 = Button(c, text="<<< PREVIOUS", bg="gray", font="arialblack 19 bold", command=sun)
	b1.place(x=600, y=600)


def sun():
	L5 = Label(c, text="_______________", font=" calibri 10", bg="deepskyblue4", padx=148, pady=9)
	L5.place(x=600, y=500)
	img = PhotoImage(file="E:\\sun.png")
	img2 = img.subsample(2, 2)
	limg2 = Label(c, image=img2, borderwidth=5, relief='raised')
	limg2.image = img2  # Keep a reference to the image to prevent it from being garbage collected
	limg2.place(x=200, y=250)

	ch1 = Radiobutton(c, text="SUN", font="arialblack 19 bold", bg="lightblue", padx=72, variable=selected_option,
					  value=9,
					  command=correct)
	ch2 = Radiobutton(c, text="MOON", font="arialblack 19 bold", bg="green", padx=62, variable=selected_option,
					  value=10, command=wrong)
	ch3 = Radiobutton(c, text="STAR", font="arialblack 19 bold", bg="red", padx=75, variable=selected_option,
					  value=11, command=wrong)
	ch4 = Radiobutton(c, text="EARTH", font="arialblack 19 bold", bg="dark orange", padx=68,
					  variable=selected_option, value=12, command=wrong)

	ch1.place(x=500, y=300)
	ch2.place(x=500, y=400)
	ch3.place(x=800, y=300)
	ch4.place(x=800, y=400)

	b1 = Button(c, text="NEXT >>>", bg="gray", font="arialblack 19 bold", command=ball)
	b1.place(x=900, y=600)
	b1 = Button(c, text="<<< PREVIOUS", bg="gray", font="arialblack 19 bold", command=cat)
	b1.place(x=600, y=600)


def cat():
	L5 = Label(c, text="_______________", font=" calibri 10", bg="deepskyblue4", padx=148, pady=9)
	L5.place(x=600, y=500)
	img = PhotoImage(file="E:\\billi.png")
	img2 = img.subsample(2, 2)
	limg2 = Label(c, image=img2, borderwidth=5, relief='raised')
	limg2.image = img2  # Keep a reference to the image to prevent it from being garbage collected
	limg2.place(x=200, y=250)

	ch1 = Radiobutton(c, text="DOG", font="arialblack 19 bold", bg="lightgreen", padx=70, variable=selected_option,
					  value=5,
					  command=wrong)
	ch2 = Radiobutton(c, text="FISH", font="arialblack 19 bold", bg="red", padx=72, variable=selected_option,
					  value=6, command=wrong)
	ch3 = Radiobutton(c, text="CAT", font="arialblack 19 bold", bg="dark orange", padx=84, variable=selected_option,
					  value=7, command=correct)
	ch4 = Radiobutton(c, text="BLUE WHALE", font="arialblack 19 bold", bg="lightblue", padx=28,
					  variable=selected_option, value=8, command=wrong)

	ch1.place(x=500, y=300)
	ch2.place(x=500, y=400)
	ch3.place(x=800, y=300)
	ch4.place(x=800, y=400)

	b1 = Button(c, text="NEXT >>>", bg="gray", font="arialblack 19 bold", command=sun)
	b1.place(x=900, y=600)


p = 0


def correct():
	global p
	z = "WELLDONE !"
	l2 = Label(c, text=z, bg="light sky blue", font="timesnewroman 19 bold", padx=115)
	l2.place(x=600, y=500)
	p = p + 10


def wrong():
	z = "OOPS! WRONG ANSWER"
	l2 = Label(c, text=z, bg="brown", font="timesnewroman 19 bold", padx=43)
	l2.place(x=600, y=500)


r = Tk()
r.title("LEARNING ADVENTURE LAND")
c = Canvas(r, width=1200, height=1200)
c.pack()
c.create_rectangle(1, 1, 1200, 1200, fill="deepskyblue4")

heading = Label(c, text=" WELCOME TO LEARN PLAY ZONE", font="algerian 45 bold", bg="skyblue3", padx=88,
				borderwidth=45, relief="groove").place(x=1, y=1)

l1 = Label(c, text="KIDS!, INSPECT THE IMAGE AND CHOOSE THE ACCURATE OPTION", bg="skyblue1",
		   font="timesnewroman 19 bold").place(x=170, y=170)

img = PhotoImage(file="E:\\apple.png")
img2 = img.subsample(2, 2)
limg = Label(c, image=img2, borderwidth=5, relief='raised').place(x=200, y=250)

# Using IntVar to keep track of the selected option
selected_option = IntVar()

# Radiobuttons instead of Checkbuttons
ch1 = Radiobutton(c, text="APPLE", font="arialblack 19 bold", bg="Red", padx=56, variable=selected_option, value=1,
				  command=correct)
ch2 = Radiobutton(c, text="ORANGE", font="arialblack 19 bold", bg="dark orange", padx=46, variable=selected_option,
				  value=2, command=wrong)
ch3 = Radiobutton(c, text="BANANA", font="arialblack 19 bold", bg="yellow", padx=56, variable=selected_option, value=3,
				  command=wrong)
ch4 = Radiobutton(c, text="WATER MELON", font="arialblack 19 bold", bg="lightgreen", padx=16, variable=selected_option,
				  value=4, command=wrong)

ch1.place(x=500, y=300)
ch2.place(x=500, y=400)
ch3.place(x=800, y=300)
ch4.place(x=800, y=400)

next = Button(c, text="NEXT >>>", bg="gray", font="arialblack 19 bold", command=cat)
next.place(x=900, y=600)

r.mainloop()
