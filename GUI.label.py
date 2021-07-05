from tkinter import *
hit = Tk()
label1 = Label(hit,text = 'hi ')
label2 = Label(hit,text = "My")
label3 = Label(hit,text= "Name")

label1.grid(row = 0 , column = 0)
label2.grid(row = 1 , column = 5)
label3.grid(row = 1 , column = 1)

hit.mainloop()

