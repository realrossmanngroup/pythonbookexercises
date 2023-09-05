import pygame.mixer
sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass
    
sound_right = sounds.Sound("hfprog_sounds/correct.wav")
sound_wrong = sounds.Sound("hfprog_sounds/wrong.wav")

asked = 0
right = 0
wrong = 0
testing = True

print("Was she right, or was she wrong? Type 1 for right, type 2 for wrong, 0 when finished!" '\n')

while testing:
    answer = int(input())
    if answer == 1:
        #sound_right.play()
        wait_finish(sound_right.play())
        asked = asked + 1
        right = right + 1
    if answer == 2:
        #sound_wrong.play()
    	wait_finish(sound_wrong.play())
    	asked = asked +1
    	wrong = wrong + 1
    elif answer == 0:
        print(f"{right} questions were answered correctly, {wrong} questions were answered wrong!")
        testing = False

