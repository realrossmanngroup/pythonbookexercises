#import sound & GUI modules & initialize them
from tkinter import *

#Set up the GUI
app = Tk()
app.title("HeadEx shipment manifest")
#####WINDOW SIZE & SCALE CODE
#Get user's screen resolution
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
#Create variable that will determine how much the program is scaled, according to screen resolution
screenwidthforscaling = int(screenwidth/700)
#Set size of window based on screen resolution
programwidth = int(0.5 * int(screenwidth))
programheight = int(0.5 * int(screenheight))
#Scale the window
app.tk.call('tk', 'scaling', screenwidthforscaling)
app.geometry(f"{programwidth}x{programheight}")
#####DONE WITH SCALING CODE

#Open file we will be saving info to
file = open("deliveries.txt")



#define the fields we will use
depotlabel = Label(app, text = "Depot: ")
depotlabel.pack(side = 'left')
depot = Entry(app)
depot.pack()
item_desc_label = Label(app, text = "Item description: ")
item_desc_label.pack()
item_desc = Entry(app)
item_desc.pack()
addresslabel = Label(app, text = "Destination address :")
addresslabel.pack()
address = Text(app)
address.pack()
app.mainloop()


#function for right button press
def right_button():
    global right
    global asked
    wait_finish(sound_right.play())
    asked = asked + 1
    right = right + 1
    num_right.set(right)

#function for wrong button press
def wrong_button():
    global wrong
    global asked
    wait_finish(sound_wrong.play())
    asked = asked +1
    wrong = wrong + 1
    num_wrong.set(wrong)
