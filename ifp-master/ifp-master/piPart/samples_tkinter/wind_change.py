from tkinter import *

def raise_frame(frame):
	frame.tkraise()

root=Tk()
root.geometry('500x500')

home=Frame(root,bg='red')
pageOne=Frame(root,bg='blue')
pageTwo=Frame(root,bg='cyan')
pageThree=Frame(root,bg='green')

for frame in (home, pageOne, pageTwo, pageThree):
	frame.grid(row=0,column=0,sticky='news')

Label(home, text='home').pack()
Button(home, text='go to page 1', command=lambda:raise_frame(pageOne)).pack()

Label(pageOne, text='page 1').pack()
Button(pageOne, text='go to page 2', command=lambda:raise_frame(pageTwo)).pack()

Label(pageTwo, text='page 2').pack()
Button(pageTwo, text='go to page 3', command=lambda:raise_frame(pageThree)).pack()

Label(pageThree, text='page 3').pack()
Button(pageThree, text='go to home', command=lambda:raise_frame(home)).pack()

raise_frame(home)
root.mainloop()