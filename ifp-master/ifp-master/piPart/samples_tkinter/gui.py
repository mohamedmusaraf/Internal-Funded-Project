import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
import os
from tkinter import font
from tkinter import messagebox as msg

win=tk.Tk()
win.geometry('500x500')
win['bg']='red'



#def openfn():
#    filename = filedialog.askopenfilename(title='open')
#    return filename


#def open_img():
img = Image.open('megacharizard.png')
img = img.resize((500, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(win, image=img)
panel.image = img
panel.place(x=0,y=0)

img2 = Image.open('wp1815588.png')
img2 = img2.resize((500, 500), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)



#btn = tk.Button(win, text='open image', command=open_img).pack()


def toggle():
	if win['bg']=='red':
		win['bg']='blue'
	else:
		win['bg']='red'

def togglePic():
	if panel['image']==img:
		panel['image']=img2
		panel.image = img2
		panel.place(x=0,y=0)
	else:
		panel['image']=img
		panel.image = img
		panel.place(x=0,y=0)




b=tk.Button(win, text='toggle', command=toggle, height=5, width=5, bg='cyan', activebackground='brown')
b.pack()

b2=tk.Button(win, text='toggle_pic', command=togglePic, height=5, width=5, bg='cyan', activebackground='brown')
b2.pack()
win.mainloop()