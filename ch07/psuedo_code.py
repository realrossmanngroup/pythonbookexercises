asked = 0
right = 0
wrong = 0
testing = True

while testing:
    answer = int(input("Was she right, or was she wrong? Type 1 for right, type 2 for wrong, 0 when finished!" '\n'))
    if answer == 1:
        #play right.wav
        asked = asked + 1
        right = right + 1
    if answer == 2:
    	#play wrong.wav
        asked = asked +1
    	wrong = wrong + 1
    elif answer == 0:
        print(f"{right} questions were answered correctly, {wrong} questions were answered wrong!")
        testing = False

