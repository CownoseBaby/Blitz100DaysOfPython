# Import the random module
import random
# Create a word list and have one randomly picked for the game
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
##########Testing code###############
#####################################
#####################################
print(f'Pssst, the solution is {chosen_word}.')
#####################################
#####################################
#####################################
# Create the blank spaces for the game
chosen_word_list = list(chosen_word)
chosen_word_length = len(chosen_word)
# Create the playing field which has the blanks showing how long the word is
playing_field = []
for letter in range(chosen_word_length):
    playing_field += "_"
print(playing_field)

# Check guessed letter
while "_" in playing_field:
    # Ask the player for a choice
    player_choice = input("Guess a letter:").lower()
    # Compare the choice to the chosen word
    for position in range(chosen_word_length):
        letter = chosen_word_list[position]
        if letter == player_choice:
            playing_field[position] = player_choice
    print(playing_field)
    if "_" not in playing_field:
        print("You Win!")