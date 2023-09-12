from tkinter import *


def flip_it():
    if flipper.get() == 1:
        print("Cool. I'm all ON, man!")
    else:
        print("Phooey. I'm OFF.")

app = Tk()
app.tk.call('tk', 'scaling', '3')
app.geometry('640x480')
app.title("Flip me!")
flipper = IntVar()
Checkbutton(app, variable = flipper, command = flip_it, text = "Flip it?").pack()
app.mainloop()
