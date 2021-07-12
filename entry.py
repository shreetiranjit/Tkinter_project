from tkinter import *
root = Tk()
e1 = Entry (root , width = 50 , fg= '#e32636' , bg = 'white' ,borderwidth= 15)
e1.pack()
def myclick() :
    textoutput = 'Hello' +  e1.get()
    myLabel = Label(root , text = textoutput)
    myLabel.pack()
    myButton = Button(root , text = textoutput)
    myButton.pack()

myButton = Button(root , text="Click me !" , command = myclick )

myButton.pack()

root.mainloop()