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

#variables for GUI size, will be set based on user's input on scaling later
global screenwidth
global screenheight

#function for right button press
def right_button():
    global right
    global asked
    wait_finish(sound_right.play())
    asked = asked + 1
    right = right + 1
    num_right.set(right)

#funtion for wrong button press
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
    #print it to the console as well. Left over from our non-GUI program
    print(f"{right} questions were answered correctly, {wrong} questions were answered wrong!")
    #Lord Stannis was a stickler for grammer, and so are we.
    if right > 1 and wrong > 1:
        l.config(text=f"{right} questions were answered correctly, {wrong} questions were answered wrong!", width = screenwidth)
    elif right == 0 and wrong == 0:
        l.config(text=f"{right} questions were answered correctly, {wrong} questions were answered wrong!", width = screenwidth)
    elif right > 1 and wrong == 0:
        l.config(text=f"{right} questions were answered correctly, {wrong} questions were answered wrong!", width = screenwidth)    
    elif right < 2 and wrong < 2:
        l.config(text=f"{right} question was answered correctly, {wrong} question was answered wrong!", width = screenwidth)
    elif right > 1 and wrong < 2:
        l.config(text=f"{right} questions were answered correctly, {wrong} question was answered wrong!", width = screenwidth)
    elif right == 0 and wrong < 2:
        l.config(text=f"{right} questions were answered correctly, {wrong} question was answered wrong!", width = screenwidth)
    elif right < 2 and wrong > 1:
        l.config(text=f"{right} question was answered correctly, {wrong} questions were answered wrong!", width = screenwidth)
    elif right < 2 and wrong == 0:
        l.config(text=f"{right} question was answered correctly, {wrong} questions were answered wrong!", width = screenwidth)
    
#ask user if they want hidpi scaling
scaling = float(input("How much scaling do you want? Type 1.0 for an old lower res screen, type 3.0 for a modern 4kish screen '\n' "))

#set width/height based on user input
#the program should, ideally, detect your screen resolution & scale accordingly
#however, I am on chapter 7 of a very basic, beginner's book on python
#this book doesn't cover scaling at all. so this crude implementation will do for now

if scaling >= 1 and scaling < 2:
    screenwidth = 450
    screenheight = 100
elif scaling >= 2 and scaling < 3:
    screenwidth = 900
    screenheight = 200
elif scaling >= 3 and scaling < 4:
    screenwidth = 1350
    screenheight = 300
elif scaling >= 4 and scaling < 7:
    screenwidth = 1700
    screenheight = 400

#Set up the GUI
app = Tk()
app.tk.call('tk', 'scaling', scaling)
app.title("Chapter 7 Gameshow")
app.geometry(f"{screenwidth}x{screenheight}")
#add buttons to it
l = Label(app, text='When you are ready, click on the buttons!', height = 3, width=screenwidth)
l.pack()
num_right = IntVar()
num_right.set(right)
num_wrong = IntVar()
num_wrong.set(wrong)
l2 = Label(app, textvariable = num_right)
l2.pack(side = 'left')
l3 = Label(app, textvariable = num_wrong)
l3.pack(side = 'right')
b1 = Button(app, text = "Right", width = 10, command = right_button)
b1.pack(side = 'left')
b2 = Button(app, text = "Wrong", width = 10, command = wrong_button)
b2.pack(side = 'right')
b3 = Button(app, text = "Finish game", width = 10, command = end_game)
b3.pack(side = 'top')
#legacy code prior to having a GUI
print("Was she right, or was she wrong? Type 1 for right, type 2 for wrong, 0 when finished!" '\n')

app.mainloop()
