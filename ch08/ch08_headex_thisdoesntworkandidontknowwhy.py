#import GUI
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter as tk
import tkinter.messagebox

#define variables we will use for functions

#define function for taking user input, storing it as a variable, then appending it to a file
def append_record():
    try:
        file = open("deliveries.txt", "a")
        file.write("Depot:\n%s\n" % (depotlocation.get()))
        file.write("Item Description:\n%s\n" % (item_desc.get()))
        file.write("Address:\n%s\n" % (address.get("1.0",END)))
        depotlocation.set(None)
    except Exception as ex:
        #app.title("Can't write to the file %s" % ex)
        tkinter.messagebox.showerror("Error!", "Can't write to the file \n %s" % ex)
        
#define function for getting depots from text file and adding it to our menu
def read_depots():
    somefile = filedialog.askopenfilename()
    depotlist = open(somefile)
    for line in depotlist:
        om1['menu'].add_command(label=line.rstrip(), command=tk._setit(depotlocation, line.strip()))
        
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
b1 = Button(app, text = "Add", width = 10, command = append_record).pack(side = BOTTOM)
b2 = Button(app, text = "Clear all", width=10, command = clear_fields).pack(side = BOTTOM)
b3 = Button(app, text = "Add depots", width=10, command = read_depots).pack(side = BOTTOM)
depotlabel = Label(app, text = "Depot:")
depotlabel.pack(side = TOP)
depotlocation = StringVar()
depotlocation.set(None)
om1 = OptionMenu(app, depotlocation, "")
om1['menu'].delete(0, END)
om1.pack(side = TOP)
item_desc_label = Label(app, text = "Item description: ").pack(side = TOP)
item_desc = Entry(app).pack()
addresslabel = Label(app, text = "Destination address :").pack()
address = Text(app).pack()

app.mainloop()

