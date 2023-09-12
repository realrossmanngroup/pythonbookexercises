from tkinter import *
from tkinter.messagebox import askokcancel
import pygame.mixer

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"

track = mixer.Sound(sound_file)

def track_start():
    track.play(loops = -1)

def track_stop():
    track.stop()

def shutdown():
    track.stop()
    if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
        app.destroy()
    
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
stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)
start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

app.protocol("WM_DELETE_WINDOW", shutdown)


app.mainloop()
