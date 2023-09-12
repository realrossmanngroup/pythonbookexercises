#Import GUI
from tkinter import *
from tkinter.messagebox import askokcancel
import pygame.mixer
import tkinter as tk

#Import & initialize mixer
mixer = pygame.mixer
mixer.init()

#Specify sound file
sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)

#Function for adjusting volume
def change_volume(v):
    track.set_volume(volume.get())
    
#Play sound if checkbox linked to track_playing intvar is clicked
def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()
        
#Stop playing music when the window is exited
def shutdown():
   track.stop()
   if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
       app.destroy()

#Make a GUI    
app = Tk()
app.title("Head First Mix")

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

#Specify volume variable
volume = DoubleVar()
volume.set(track.get_volume())
volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0, resolution = 0.05, command = change_volume, label = "Volume", orient = HORIZONTAL, length = 0.4 * programwidth)
volume_scale.pack(side = BOTTOM)

#Make checkbox for playing music
track_playing = IntVar()
Checkbutton(app, variable = track_playing, command = track_toggle, text = "50459_M_RED_Nephlimizer.wav").pack()

#Change 
app.protocol("WM_DELETE_WINDOW", shutdown)


app.mainloop()
