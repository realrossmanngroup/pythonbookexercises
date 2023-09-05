#import sound and GUI modules & initialize them
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

#funtion for wrong button press
def wrong_button():
    global wrong
    global asked
    wait_finish(sound_wrong.play())
    asked = asked +1
    wrong = wrong + 1

#function for ending the game
def end_game():
    global right
    global wrong
    global asked
    print(f"{right} questions were answered correctly, {wrong} questions were answered wrong!")
    testing = False  

#ask user if they want hidpi scaling
scaling = float(input("How much scaling do you want? Type 1.0 for an old lower res screen, type 3.0 for a modern 4kish screen '\n' "))
    
#Set up the GUI
app = Tk()
#Make GUI look decent on modern monitors w/ higher resolution based on user input
app.tk.call('tk', 'scaling', scaling)
app.title("Chapter 7 Gameshow")
if scaling >= 1 and scaling < 2:
    app.geometry('450x100+200+100')
elif scaling >= 2 and scaling < 3:
    app.geometry('900x200+200+100')
elif scaling >= 3 and scaling < 4:
    app.geometry('900x200+200+100')
elif scaling >= 4 and scaling < 7:
    app.geometry('1350x300+200+100')
#add buttons to it
b1 = Button(app, text = "Right", width = 10, command = right_button)
b1.pack(side = 'left')
b2 = Button(app, text = "Wrong", width = 10, command = wrong_button)
b2.pack(side = 'right')
b3 = Button(app, text = "Finish game", width = 10, command = end_game)
b3.pack(side = 'top')
#prompt gameshow host to tell us what's going on
print("Was she right, or was she wrong? Type 1 for right, type 2 for wrong, 0 when finished!" '\n')

app.mainloop()



#main program runs to receive input from gameshow host, keep track of questions, play sounds

while testing:
    answer = int(input())
    if answer == 1:
        wait_finish(sound_right.play())
        asked = asked + 1
        right = right + 1
    if answer == 2:
    	wait_finish(sound_wrong.play())
    	asked = asked +1
    	wrong = wrong + 1
    elif answer == 0:
        print(f"{right} questions were answered correctly, {wrong} questions were answered wrong!")
        testing = False

