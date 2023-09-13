from tkinter import *
import pygame
import tkinter.filedialog as filedialog
import os

def create_gui(app, mixer):
    def track_toggle():
        if track_playing.get() ==1:
            track.play(loops = -1)
        else:
            track.stop()

    #get volume from DoubleVar volume below
    def change_volume(v):
        track.set_volume(volume.get())

    #Ask user for filename of new track to be added
    newsound = filedialog.askopenfilename()
    track = mixer.Sound(newsound)
    #Keep track of whether the track is playing within checkbox
    track_playing = IntVar()
    track_playing.set(0)
    #Create play button for track
    trackbutton = Checkbutton(app, variable = track_playing, command = track_toggle, text = os.path.basename(newsound))
    trackbutton.pack(side = LEFT)
    #Keep track of volume for track
    volume = DoubleVar()
    volume.set(track.get_volume())
    #Create volume button for track
    volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0, resolution = 0.05, command = change_volume, label = f"Vol {os.path.basename(newsound)}", orient = HORIZONTAL, length=500)
    volume_scale.pack(side = RIGHT)

#Stop playing music when the window is exited

def shutdown():
   track.stop()
   if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
       app.destroy()
