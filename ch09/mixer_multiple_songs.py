#Import GUI
from tkinter import *
from tkinter.messagebox import askokcancel
import pygame.mixer
import tkinter as tk
import tkinter.filedialog as filedialog
import os
from sound_panel import *
global tracknumber

#Make a GUI    
app = Tk()
app.title("Head First Mix")
#Get user's screen resolution
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
programwidth = int(0.32 * int(screenwidth))
programheight = int(0.45 * int(screenheight))
#Create variable that will determine how much the program is scaled, according to screen resolution
screenwidthforscaling = screenwidth/1400
app.tk.call('tk', 'scaling', screenwidthforscaling)
app.geometry(f"{programwidth}x{programheight}")

#Import & initialize mixer
mixer = pygame.mixer
mixer.init()

#Button for choosing music file
b1 = Button(app, text = "Add track!", width=10, command = lambda:create_gui(app, mixer)).pack(side = BOTTOM)

#Stop playing music when the window is exited

def shutdown():
   track.stop()
   if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
       app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
