### CONTENT OF THIS REPO

#GUESS GAME
Here's how the game works: the Guess game works

The program generates a random number between 1 and 100 using the random.randint() function.
The program prompts the user to guess the number and enters a loop.
Inside the loop, the program checks whether the user's input is a valid number using the isdigit() method.
If the input is not a valid number, the program prompts the user to enter a valid number again using continue to skip the rest of the loop and start from the beginning.
If the input is a valid number, the program converts it to an integer using int() and increments the attempts counter.
If the user's guess is too low, the program prints "Too low. Guess again."
If the user's guess is too high, the program prints "Too high. Guess again."
If the user's guess is correct, the program exits the loop and prints "Congratulations! You guessed the number in {attempts} attempts."

# RANDOM GAME
Here's how the game works:

The program prints a welcome message and prompts the user to choose their weapon: rock, paper, or scissors.
The program stores the possible options in a list called options and randomly selects one option for the computer using random.choice().
The program prompts the user to enter their choice and converts the input to lowercase using the lower() method.
The program prints the computer's choice using an f-string.
The program uses if and else statements to compare the player's choice to the computer's choice.
If the player's choice is the same as the computer's choice, the program prints "It's a tie!"
If the player's choice beats the computer's choice, the program prints "You win!"
If the computer's choice beats the player's choice, the program prints "Computer wins!"
