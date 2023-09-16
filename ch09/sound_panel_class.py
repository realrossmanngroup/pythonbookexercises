from tkinter import *
import pygame.mixer
import tkinter.filedialog as filedialog
import os

class SoundPanel(Frame):
    def __init__(self, app, mixer, sound_file):
        Frame.__init__(self, app)
        self.track = mixer.Sound(sound_file)
        self.track_playing = IntVar()
        track_button = Checkbutton(self, variable = self.track_playing, command = self.track_toggle, text = os.path.basename(sound_file))
        track_button.pack(side = LEFT)
        self.volume = DoubleVar()
        self.volume.set(self.track.get_volume())
        volume_scale = Scale(self, variable = self.volume, from_ = 0.0, to = 1.0,
resolution = 0.1, command = self.change_volume, label = "Volume", width = 30, orient = HORIZONTAL)
        volume_scale.pack(side = RIGHT)

    def track_toggle(self):
        if self.track_playing.get() == 1:
            self.track.play(loops = -1)
        else:
            self.track.stop()

    def change_volume(self, v):
        self.track.set_volume(self.volume.get())
        
