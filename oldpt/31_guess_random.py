from random import randint
secret = randint(1, 10)
guess = 0
print("Welcome!")
while guess != secret:
        g = input("Guess the number: ") 
        guess = int(g)
        if guess > secret:
                print("Too high! Try again!")
        if guess < secret:
                print("Too low! Try again!")
print("Game over, you got it you cunt!")
print(secret)
