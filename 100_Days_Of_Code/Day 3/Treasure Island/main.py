print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print("So you arrive onto treasure island looking for the mysterious and magical treasure that is said to grant immortality.")
print("As you get onto the dock, you see there are two paths to take.")
print("First is a path to the left which takes you down a river, or a path to the right which appears to be a path well traverse.")
if input("Would you like to go left or right? ").lower() == "left":
    print("So you follow the river for miles and come to a lake.")
    print("You see out in the middle of the lake is a castle like you have never seen.")
    print("It's beauty is like none other.")
    if input("You can swim across the lake or sit and admirer the castle. Sit or Swim? ").lower() == "sit":
        print("As your sitting and just admiring the castle, you magically appear in the castle's courtyard.")
        print("As your walking up to the castle's interior wall, you see three doors. Red, Yellow, and Blue.")
        door_choice = input("Which door would you like to open? ")
        if door_choice.lower() == "red":
            print("A huge wall of fire shoots out the door and burns you to death.")
            print("The journey is over, better luck next time.")
        elif door_choice.lower() == "blue":
            print("You found the castle's guardian and get killed.")
            print("The journey is over, better luck next time.")
        elif door_choice.lower() == "yellow":
            print("Congratulations you found the foundation of immortality! You Win!")
        else:
            print("You get teleported back to your boat.")
            print("The journey is over, better luck next time.")
    else:
        print("You fail to make it across the lake so you drown. The journey is over, better luck next time.")
else:
    print("You find some bandits along the road and they attack you. The journey is over, better luck next time.")



