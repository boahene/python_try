import random

print("Let's play Rock, Paper, Scissors!")
print("Choose your weapon: rock, paper, or scissors.")

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
player_choice = input("Your choice: ").lower()

print(f"Computer chose {computer_choice}.")

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")
