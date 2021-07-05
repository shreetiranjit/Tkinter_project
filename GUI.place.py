from tkinter import*
geo = Tk()
geo.geometry('200x250')

name = Label(geo , text = 'Name').place (x = 30 ,y = 50)
address = Label(geo ,text = 'Address').place(x=30 , y =90)
contact = Label(geo , text = 'Contact').place(x=30,y=130)
n1 = Entry(geo).place(x=80 ,y =50)
a2 = Entry(geo).place(x=80,y=90)
c3 = Entry(geo).place(x=90,y=130)

geo.mainloop()
