from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox

root = Tk()
root.title('check button')
def show():
    myLabel = Label(root, text = var.get()).pack()

var = StringVar()
#value of onvalue and offvalue can be different
checkbutton = Checkbutton(root,text = 'Check!!!' , variable = var , onvalue = 'ON' , offvalue = 'OFF')
#Automatically selection on the box will be removed.
checkbutton.deselect()
checkbutton.pack()

myButton = Button(root, text = 'Show Selection' , command = show).pack()

root.mainloop()
