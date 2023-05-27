# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
#Menu Items
pizza_small = 15
pizza_medium = 20
pizza_large = 25
pizza_pepperoni_small = 2
pizza_pepperoni_medium = 3
pizza_pepperoni_large = 3
pizza_extra_cheese = 1

if size == "S":
    bill += pizza_small
    if add_pepperoni == "Y":
        bill += pizza_pepperoni_small
    if extra_cheese == "Y":
        bill += pizza_extra_cheese
elif size == "M":
    bill += pizza_medium
    if add_pepperoni == "Y":
        bill += pizza_pepperoni_medium
    if extra_cheese == "Y":
        bill += pizza_extra_cheese
else:
    bill += pizza_large
    if add_pepperoni == "Y":
        bill += pizza_pepperoni_large
    if extra_cheese == "Y":
        bill += pizza_extra_cheese

print(f"Your final bill is: ${bill}.")