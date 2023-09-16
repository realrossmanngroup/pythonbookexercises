#Import GUI
from tkinter import *
from tkinter.messagebox import askokcancel
import pygame.mixer
import tkinter as tk
import tkinter.filedialog as filedialog
import os
from sound_panel_class import *
global tracknumber
from tkinter import *
from sound_panel_class import *
import pygame.mixer
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

dirList = os.listdir(".")

for fname in dirList:
   if fname.endswith(".wav"):
      panel = SoundPanel(app, mixer, fname)
      panel.pack()
      
def shutdown():
   #track.stop()
   app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()


