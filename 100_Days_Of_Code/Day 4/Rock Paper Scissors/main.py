rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

print("Welcome to a game of Rock, Paper, Scissors.")
choices = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(input("Please make a choice. 0 for Rock, 1 for Paper, 2 for Scissors\n"))

print(f"You choose {choices[player_choice]}")
print(f"Computer choose {choices[computer_choice]}")

if choices[player_choice] == choices[computer_choice]:
    print("It's a draw!")
elif choices[computer_choice] == choices[player_choice - 1]:
    print("You Win!")
else:
    print("You Lose!")
