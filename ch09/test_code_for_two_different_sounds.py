#Import GUI
from tkinter import *
from tkinter.messagebox import askokcancel
import pygame.mixer
import tkinter as tk
import tkinter.filedialog as filedialog

#Import & initialize mixer
mixer = pygame.mixer
mixer.init()

#Specify sound file
sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)
whattoplay = track

whattoplay.play()

soundfile2 = "othersong.wav"
track2 = mixer.Sound(soundfile2)

whattoplay = track2

whattoplay.play()
