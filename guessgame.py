import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while guess != number:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    attempts += 1
    if guess < number:
        print("Too low. Guess again.")
    elif guess > number:
        print("Too high. Guess again.")

print(f"Congratulations! You guessed the number in {attempts} attempts."
