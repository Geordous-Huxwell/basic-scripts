from tkinter import *
from tkinter import messagebox

def enterButtonAction():
	messagebox.showinfo("Title","Hello, World!")

root = Tk()
root.title("Test app")

btn_1 = Button(root,text = "1")
btn_1.grid(row = 0, column = 0,padx = 0,pady = 0,ipadx = 0,ipady = 0)

btn_2 = Button(root,text = "2")
btn_2.grid(row = 0, column = 1)

btn_3 = Button(root,text = "3")
btn_3.grid(row = 0, column = 2)

btn_4 = Button(root,text = "4")
btn_4.grid(row = 1, column = 0)

btn_5 = Button(root,text = "5")
btn_5.grid(row = 1, column = 1)

btn_6 = Button(root,text = "6")
btn_6.grid(row = 1, column = 2)

btn_7 = Button(root,text = "7")
btn_7.grid(row = 2, column = 0)

btn_8 = Button(root,text = "8")
btn_8.grid(row = 2, column = 1)

btn_9 = Button(root,text = "9")
btn_9.grid(row = 2, column = 2)

btn_enter = Button(root, text = "This is the enter button",command = enterButtonAction)
btn_enter.grid(row = 0,column = 3,rowspan = 3,sticky = "NS")

root.mainloop()