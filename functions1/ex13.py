"""Write a program able to play the - game, where the number to be guessed
is randomly chosen between 1 and 20. This is how it should work when run
in a terminal:"Guess the number"""
import random

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

guess_the_number()
