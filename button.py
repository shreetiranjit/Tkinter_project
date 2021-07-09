from tkinter import*
root = Tk()

def myclick():
    mylabel = Label(root , text = "You have clicked the button.")
    mylabel.pack()

myButton = Button(root , text = 'click me !' , command = myclick)
myButton.pack()

root.mainloop()