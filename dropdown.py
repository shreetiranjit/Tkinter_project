from tkinter import *

root = Tk()
root.title('Drop down')
def show():
    myLabel = Label(root , text = clicked.get()).pack()

clicked = StringVar()
#sets the default value on screen
clicked.set('Monday')

drop = OptionMenu(root ,clicked , 'Monday' , 'tuesday')
drop.pack()

myButton = Button(root , text = 'Show selection' , command= show).pack()



#or



def show1():
    myLabel1 = Label (root , text = clicked1.get()).pack()

options= ['monday' , 'Tuesday' , 'Wednesday']
clicked1 = StringVar()
clicked1.set('monday')

drop1 = OptionMenu(root , clicked1 ,*options)
drop1.pack()

myButton1 =Button(root , text = 'Show the selection' , command= show1).pack()

root.mainloop()
