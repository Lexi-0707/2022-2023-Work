import random

# Alexis Ellis 1/12/23

counter = 0 

print("Welcome to a 'Guess my number' game. The computer will pick a random number between 1 - 100.")
print("Try and guess the number with the least amount of guesses, at the end you will be told how many it took you. Good luck!")

randomNumber = random.randint(1, 100)

guess = int(input("Please enter a guess. "))

while guess != randomNumber:
    if guess > randomNumber:
        print("Guess lower. ")
    else:
        print("Guess higher. ")
    counter += 1
    guess = int(input("Please enter a guess."))

print("Congrats on guessing the correct number. Your total numbers of guesses is", counter)
