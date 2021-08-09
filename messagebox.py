from tkinter import*
from PIL import ImageTk , Image
from tkinter import  messagebox
root = Tk()
root.title('Message box')

def popup():
    messagebox.showinfo('This is my Pop Up.')

Button(root , text = 'PopUp' , command = popup).pack()
root.mainloop()