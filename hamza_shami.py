import random

def play_game():
    print(" Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = input(" Guess a number between 1 and 10: ")

        if not guess.isdigit():
            print(" Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print(" Too low!")
        elif guess > secret_number:
            print(" Too high!")
        else:
            print(f" Correct! The number was {secret_number}. You guessed it in {attempts} attempts.")
            break

play_game()