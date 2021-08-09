from tkinter import *


root = Tk()
root.title('Slider')


#Vertical Slider

vertical = Scale(root, from_=0, to=450)
vertical.pack()

#Horizontal Slider
horizontal = Scale(root, from_=0, to=450, orient=HORIZONTAL)
horizontal.pack()

#my_label = Label(root, text=horizontal.get()).pack()
#Function slide craeated
def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    my_label2 = Label(root,text = vertical.get()).pack()

    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#Function called
my_btn = Button(root, text="Click Me", command=slide).pack()

mainloop()

