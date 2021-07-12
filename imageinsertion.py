from tkinter import *
from PIL import ImageTk , Image

root = Tk()
root.title("image insertion")
root.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/ne.ico')

my_image = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/download.png'))
my_label = Label(image = my_image)
my_label.pack()

button_quit = Button(root , text ="EXIT" , command =root.quit,width = 25 )
button_quit.pack()

root.mainloop()


