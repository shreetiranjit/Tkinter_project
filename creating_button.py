from tkinter import *
create = Tk()
#button without any function
myButton = Button(create , text = "Click Me")
myButton.pack()
#state disabled button
myButton1 = Button(create , text = "Click" , state = DISABLED)
myButton1.pack()
#button x and y padding
myButton2 = Button(create , text ='Click'  , padx = 50)
myButton2.pack()
myButton3 = Button(create , text = "Click" , padx =50 ,pady = 50 )
myButton3.pack()

create.mainloop()
