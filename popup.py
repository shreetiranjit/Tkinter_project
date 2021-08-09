from tkinter import*
from PIL import ImageTk , Image
from tkinter import messagebox
root = Tk()
root.title('Message Box')
root.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/m.ico')
def popup():
    response = messagebox.askyesno('This is my popup ' , 'Hello World')
    Label(root , text=response).pack
    if response == 1 :
        Label(root, text =" YES").pack()
    else:
        Label(root, text=" NO").pack()

Button(root , text = 'Popup' , command = popup ).pack()

root.mainloop()