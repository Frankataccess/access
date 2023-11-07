def letter_to_number(letter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    number = letters.index(letter)
    return number

def number_to_letter(index):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters[index]

def shift(letter):
    if letter.islower():
        n = letter_to_number(letter)
        return number_to_letter((n + 13) % 26)
    elif letter.isupper():
        n = letter_to_number(letter.lower())
        shifted_char = number_to_letter((n + 13) % 26)
        return shifted_char.upper()
    else:
        # If the character is not a letter, keep it unchanged
        return letter

def rot13(string):
    ciphertext = ""
    for letter in string:
        ciphertext += shift(letter)
    return ciphertext

plaintext = input("enter a password: ")
ciphertext = rot13(plaintext)
print(ciphertext)