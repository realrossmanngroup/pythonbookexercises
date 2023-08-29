print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
	print("You win!")
else:
        if guess > 5:
                print("Too high! Try again!")
        else:
                print("Too low! Try again!")
print("Game over!")
