from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root= Tk()
root.title('Create Window ')



def open() :
    global my_img
    top = Toplevel()
    top.title('Check new window')
    my_img = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/s.png'))
    my_label = Label(top, image = my_img).pack()

    btn2 = Button(top, text = 'Close Window' , command = top.destroy).pack()

def open1():
    global my_img
    top2 = Toplevel()
    top2.title('Check new window')

    my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/v.png'))


    my_label1 = Label(top2, image=my_img1).pack()
    btn3 = Button(top2, text='Close Window', command=top2.destroy).pack()


btn = Button(root, text = 'Open', command = open).pack()
btn1 = Button(root, text = 'Open', command = open1).pack()


root.mainloop()
