from tkinter import*
root = Tk()

name = Label(root, text='NAME').grid(row= 0, column = 0)
n1 = Entry(root).grid(row = 0 , column = 1)

password = Label(root, text='Password').grid(row=1 , column = 0)
p2 = Entry(root).grid(row=1, column = 1)


submit = Button(root, text = 'Submit').grid(row = 4 , column = 1)


root.mainloop()