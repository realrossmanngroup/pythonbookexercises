#import sound & GUI modules & initialize them
from tkinter import *
import pygame.mixer
sounds = pygame.mixer
sounds.init()

#function that waits until sound is finished to continue playing.
#type wait_finish(soundnamehere.play()) to play a sound
def wait_finish(channel):
    while channel.get_busy():
        pass
#define main program sounds
sound_right = sounds.Sound("hfprog_sounds/correct.wav")
sound_wrong = sounds.Sound("hfprog_sounds/wrong.wav")

#set variables storing count of right & wrong answers to 0
asked = 0
right = 0
wrong = 0
testing = True

#function for right button press
def right_button():
    global right
    global asked
    wait_finish(sound_right.play())
    asked = asked + 1
    right = right + 1
    num_right.set(right)

#function for wrong button press
def wrong_button():
    global wrong
    global asked
    wait_finish(sound_wrong.play())
    asked = asked +1
    wrong = wrong + 1
    num_wrong.set(wrong)
    
#function for ending the game
def end_game(): 
    global right
    global wrong
    global asked
    #Lord Stannis was the one true King of Westeros, and he demanded proper grammer. We honor him with the following code:
    if right > 1 and wrong > 1:
        l.config(text=f"{right} questions were answered correctly, {wrong} questions were answered wrong!", width = programwidth)
    elif right == 0 and wrong == 0:
        l.config(text=f"{right} questions were answered correctly, {wrong} questions were answered wrong!", width = programwidth)
    elif right > 1 and wrong == 0:
        l.config(text=f"{right} questions were answered correctly, {wrong} questions were answered wrong!", width = programwidth)   
    elif right > 0 and right < 2 and wrong < 2 and wrong > 0:
        l.config(text=f"{right} question was answered correctly, {wrong} question was answered wrong!", width = programwidth)
    elif right > 1 and wrong < 2:
        l.config(text=f"{right} questions were answered correctly, {wrong} question was answered wrong!", width = programwidth)
    elif right == 0 and wrong < 2:
        l.config(text=f"{right} questions were answered correctly, {wrong} question was answered wrong!", width = programwidth)
    elif right > 0 and right < 2 and wrong > 1:
        l.config(text=f"{right} question was answered correctly, {wrong} questions were answered wrong!", width = programwidth)
    elif right < 2 and wrong == 0:
        l.config(text=f"{right} question was answered correctly, {wrong} questions were answered wrong!", width = programwidth)
    elif right == 0 and wrong > 1:
        l.config(text=f"{right} question were answered correctly, {wrong} questions were answered wrong!", width = programwidth)
#Set up the GUI
app = Tk()
app.title("Chapter 7 Gameshow")
#Get user's screen resolution
screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
#Create variable that will determine how much the program is scaled, according to screen resolution
screenwidthforscaling = int(screenwidth/700)
#Set size of window based on screen resolution
programwidth = int(0.5 * int(screenwidth))
programheight = int(0.25 * int(screenheight))
#Scale the window
app.tk.call('tk', 'scaling', screenwidthforscaling)
app.geometry(f"{programwidth}x{programheight}")
#add buttons to it
l = Label(app, text='When you are ready, click on the buttons!', height = 3, width=programwidth)
l.pack()
#Make intvars and set them equal to the variables that count right & wrong answers
num_right = IntVar()
num_right.set(right)
num_wrong = IntVar()
num_wrong.set(wrong)
#Place the labels that will show the count of right & wrong answers within the GUI
l2 = Label(app, textvariable = num_right)
l2.pack(side = 'left')
l3 = Label(app, textvariable = num_wrong)
l3.pack(side = 'right')
#Make the buttons the user will click to count right & wrong answers
b1 = Button(app, text = "Right", width = 10, command = right_button)
b1.pack(side = 'left')
b2 = Button(app, text = "Wrong", width = 10, command = wrong_button)
b2.pack(side = 'right')
b3 = Button(app, text = "Finish game", width = 10, command = end_game)
b3.pack(side = 'top')

app.mainloop()
