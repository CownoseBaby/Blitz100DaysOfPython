import functions
import art

print(art.logo)

end_of_program = False
while not end_of_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    functions.caesar(text, shift, direction)
    restart_program = input("Would you like to restart the cipher program? Yes or No?\n").lower()
    if restart_program == "no":
        end_of_program = True
        print("Good Bye")
