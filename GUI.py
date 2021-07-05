from tkinter import *
window = Tk()
windowbutton = Button(window , text = "LEFT", fg = 'PURPLE')
windowbutton.pack(side = LEFT)
window1button = Button(window , text = "Right", fg = 'Blue')
window1button.pack(side = RIGHT)
window2button = Button(window , text = 'Top' , fg = 'Black')
window2button.pack (side = TOP)
window3button = Button(window , text = 'Bottom' , fg = 'Red')
window3button.pack(side = BOTTOM)

mainloop()