# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

print("Let's flip a coin!")

random_number = random.randint(1, 2)

if random_number == 1:
    print("Heads")
elif random_number == 2:
    print("Tails")