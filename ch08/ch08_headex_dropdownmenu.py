#import GUI
from tkinter import *
import tkinter.filedialog as filedialog

#define variables we will use for functions
global depot_fieldretrieve
global address_fieldretrieve
global item_desc_fieldretrieve

#define function for taking user input, storing it as a variable, then appending it to a file
def append_record():
    file = open("deliveries.txt", "a")
    depot_fieldretrieve = depotlocation.get()
    item_desc_fieldretrieve = item_desc.get()
    address_fieldretrieve = address.get("1.0",END)
    file.write("Depot:\n%s\n" % (depot_fieldretrieve))
    file.write("Item Description:\n%s\n" % (item_desc_fieldretrieve))
    file.write("Address:\n%s\n" % (address_fieldretrieve))
    depotlocation.set(None)

#define function for getting depots from text file and adding it to our menu
def read_depots():
    depots = []
    depots.clear()
    somefile = filedialog.askopenfilename()
    depotlist = open(somefile)
    for line in depotlist:
        om1['menu'].add_command(label=line.rstrip())

#define function for clearing fields when done
def clear_fields():
    #clear the variable containing list of depots
    om1['menu'].delete(0, END)
    #clear the dropdown menu list of depots
    depotlocation.set("")
    #deselect depots
    depotlocation.set(None)
    #delete text in fields
    item_desc.delete(0, END)
    address.delete("1.0", END)

#Set up the GUI
app = Tk()
app.title("HeadEx shipment manifest")

#####WINDOW SIZE & SCALE CODE
#Get user's screen resolution
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()

#Create variable that will determine how much the program is scaled, according to screen resolution
screenwidthforscaling = screenwidth/1000

#Set size of window based on screen resolution
programwidth = int(0.32 * int(screenwidth))
programheight = int(0.45 * int(screenheight))

#Scale the window
app.tk.call('tk', 'scaling', screenwidthforscaling)
app.geometry(f"{programwidth}x{programheight}")
#####DONE WITH SCALING CODE

#define the fields we will use, begin loop
b1 = Button(app, text = "Add", width = 10, command = append_record)
b1.pack(side = 'bottom')
b2 = Button(app, text = "Clear", width=10, command = clear_fields)
b2.pack(side = 'bottom')
b3 = Button(app, text = "Read depots", width=10, command = read_depots)
b3.pack(side = 'bottom')
depotlabel = Label(app, text = "Depot:")
depotlabel.pack(side = 'top')
depotlocation = StringVar()
depotlocation.set(None)
om1 = OptionMenu(app, depotlocation, "")
om1.pack(side = 'top')
item_desc_label = Label(app, text = "Item description: ")
item_desc_label.pack(side = 'top')
item_desc = Entry(app)
item_desc.pack()
addresslabel = Label(app, text = "Destination address :")
addresslabel.pack()
address = Text(app)
address.pack()

app.mainloop()
