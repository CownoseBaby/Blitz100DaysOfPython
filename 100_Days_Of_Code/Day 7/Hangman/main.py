# Import the random module
import random
import hangman_words
import hangman_art

# Create a word list and have one randomly picked for the game
chosen_word = random.choice(hangman_words.word_list)
chosen_word_list = list(chosen_word)
chosen_word_length = len(chosen_word)
player_guess_list = []
lives = 6
end_of_game = False
print(hangman_art.logo)
# Create the playing field which has the blanks showing how long the word is
playing_field = []
for letter in range(chosen_word_length):
    playing_field += "_"
print(playing_field)

# Check guessed letter
while not end_of_game:
    # Ask the player for a choice
    player_guess = input("Guess a letter:").lower()
    # Inform user if letter has been guessed already
    while player_guess in player_guess_list:
        print(f"You have already guessed {player_guess}. Please try another letter")
        player_guess = input("Guess a letter:").lower()
    # Add guessed letter to a list
    player_guess_list += player_guess
    # Compare the choice to the chosen word
    for position in range(chosen_word_length):
        letter = chosen_word_list[position]
        if letter == player_guess:
            playing_field[position] = player_guess
    if player_guess not in chosen_word:
        print(f"The letter {player_guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You Lose!")
            end_of_game = True
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(playing_field)}")
    if "_" not in playing_field:
        print("You Win!")
        end_of_game = True
    print(hangman_art.stages[lives])