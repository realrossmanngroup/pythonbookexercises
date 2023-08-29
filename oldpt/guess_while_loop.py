print("Welcome!")
g = 0
guess = int(g)
while guess != 5:
        g = input("Guess the number: ")
        guess = int(g)
        if guess > 5:
                print("Too high! Try again!")
        if guess < 5:
                print("Too low! Try again!")
        else:
                print("Invalid input puto!")
print("Game over, you got it you cunt!")
