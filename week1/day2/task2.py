# Write a guessing game: random number 1–10, user guesses until correct.
import random

secret_number = random.randint(1, 10)
guess = None
tries = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct ! You guessed it in {tries} tries.")
