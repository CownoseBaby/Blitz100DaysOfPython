alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    shift_amount = shift_amount % len(alphabet)
    for char in start_text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            if cipher_direction == "encode":
                new_index = letter_index + shift_amount
            elif cipher_direction == "decode":
                new_index = letter_index - shift_amount
            end_text += alphabet[new_index]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


# def encrypt(plain_text, shift_amount):
#     encoded_message = ''
#     for letter in plain_text:
#         letter_index = alphabet.index(letter)
#         encoded_index = letter_index + shift_amount
#         encoded_letter = alphabet[encoded_index]
#         encoded_message += encoded_letter
#     print(f"The encoded text is {encoded_message}")


# def decrypt(cipher_text, shift_amount):
#     plain_text = ''
#     for letter in cipher_text:
#         letter_index = alphabet.index(letter)
#         decoded_index = letter_index - shift_amount
#         encoded_letter = alphabet[decoded_index]
#         plain_text += encoded_letter
#     print(f"The decoded text is {plain_text}")
