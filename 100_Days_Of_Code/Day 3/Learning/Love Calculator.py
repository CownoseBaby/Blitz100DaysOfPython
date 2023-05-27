# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

# Need to count the letters that speed out "true love" in both names
count_t = lower_case_name1.count('t') + lower_case_name2.count('t')
count_r = lower_case_name1.count('r') + lower_case_name2.count('r')
count_u = lower_case_name1.count('u') + lower_case_name2.count('u')
count_e = lower_case_name1.count('e') + lower_case_name2.count('e')

count_l = lower_case_name1.count('l') + lower_case_name2.count('l')
count_o = lower_case_name1.count('o') + lower_case_name2.count('o')
count_v = lower_case_name1.count('v') + lower_case_name2.count('v')
# E for love is accounted for already

# Need to put the result together and find the percentage
result_word1 = count_t + count_r + count_u + count_e
result_word2 = count_l + count_o + count_v + count_e
result_total = int(f"{result_word1}{result_word2}")

if result_total < 10 or result_total > 90:
    print(f"Your score is {result_total}, you go together like coke and mentos.")
elif result_total > 40 and result_total < 50:
    print(f"Your score is {result_total}, you are alright together.")
else:
    print(f"Your score is {result_total}.")