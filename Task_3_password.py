import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Password Generator!")

length = int(input("Enter the desired length of the password: "))

use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

print(f"Generated password: {password}")
