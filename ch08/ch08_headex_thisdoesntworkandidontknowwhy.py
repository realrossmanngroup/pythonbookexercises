#import GUI
from tkinter import *

#define variables we will use for functions
global depot_fieldretrieve
global address_fieldretrieve
global item_desc_fieldretrieve

#define function for taking user input, storing it as a variable, then appending it to a file
def append_record():
    #Open file we will be saving info to
    file = open("deliveries.txt", "a")
    depot_fieldretrieve = depot.get()
    item_desc_fieldretrieve = item_desc.get()
    address_fieldretrieve = address.get("1.0",END)
    file.write("Depot:\n%s\n" % (depot_fieldretrieve))
    file.write("Item Description:\n%s\n" % (item_desc_fieldretrieve))
    file.write("Address:\n%s\n" % (address_fieldretrieve))

#define function for clearing fields when done
def clear_fields():
    depot.delete(0, END)
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
screenwidthforscaling = int(screenwidth/700)

#Set size of window based on screen resolution
programwidth = int(0.5 * int(screenwidth))
programheight = int(0.5 * int(screenheight))

#Scale the window
app.tk.call('tk', 'scaling', screenwidthforscaling)
app.geometry(f"{programwidth}x{programheight}")
#####DONE WITH SCALING CODE

#define the fields we will use
####
####
####
#### WHY DOES THIS NOT WORK WHEN I USE .pack(side = 'bottom') AT THE END OF THE LINE? WHY DOES IT ONLY WORK IF I DO b2.pack(side = 'bottom')  ON A NEW LINE?
b1 = Button(app, text = "Add", width = 10, command = append_record).pack(side = 'bottom')
b2 = Button(app, text = "Clear", width=10, command = clear_fields).pack(side = 'bottom')
depotlabel = Label(app, text = "Depot: ").pack(side = 'top')
#### WHY DOES THIS NOT WORK WHEN I USE .pack() AT THE END OF THE LABEL? WHY DOES IT ONLY WORK WHEN I TYPE depot.pack() ON A NEW LINE?
depot = Entry(app).pack()
item_desc_label = Label(app, text = "Item description: ").pack()
item_desc = Entry(app).pack()
addresslabel = Label(app, text = "Destination address :").pack()
address = Text(app).pack()

app.mainloop()


