from tkinter import *
root = Tk()
root.title ('CHOOSE GENDER')
MODES = [
    ("MALE",'M'),
    ("FEMALE" , 'F'),
    ('Others' , 'O'),
    ('None', ' N')
]
gender = StringVar()
gender.set(" ")


for text, mode in MODES:
    Radiobutton(root ,text =text , variable = gender , value= mode).pack(anchor= W )

def clicked(value):
    myLabel = Label(root , text =value )
    myLabel.pack()


myButton = Button (root , text = 'click me' , command = lambda : clicked(gender.get())).pack()



root.mainloop()
