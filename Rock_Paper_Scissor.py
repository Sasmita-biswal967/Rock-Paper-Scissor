import random

# ASCII art for Rock, Paper, and Scissors
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of ASCII art for Rock, Paper, and Scissors
game_img = [Rock, Paper, Scissors]

# List of choices for the user
choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock Paper Scissor.")

user_score = 0
computer_score = 0

while True:
    # Getting the user's choice
    user_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors, or -1 to exit: "))

    # Checking if the user wants to exit
    if user_choice == -1:
        print("Thanks for playing!")
        print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
        if user_score > computer_score:
            print("You are the winner!")
        elif user_score < computer_score:
            print("Computer is the winner!")
        else:
            print("It's a tie!")
        break

    # Checking if the user's choice is valid
    if user_choice < 0 or user_choice > 2:
        print("Your choice is invalid. Please choose a number between 0 and 2.")
        continue

    # Printing the user's choice
    print(f"You chose: {choices[user_choice]}")
    print(game_img[user_choice])

    # Getting the computer's choice
    comp_choice = random.randint(0, 2)

    # Printing the computer's choice
    print(f"Computer chose: {choices[comp_choice]}")
    print(game_img[comp_choice])

    # Determining the winner
    if user_choice == comp_choice:
        print("It's a draw!!!")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
        print("Congrats, You win this round!!!")
        user_score += 1
    else:
        print("Oops, You lose this round!")
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}\n")