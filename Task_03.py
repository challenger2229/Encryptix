# Task_03 : this task is all about generating a password generator which will generate random sequesnce of passwords for user

# the program works as follows- a specified lenght of password is inputted by the user and the program generates and displays a random sequence password on the screen

# the only basic limit is that the password should begreater than 4 characters



print("------------------------------PASSWORD GENERATOR------------------------------")

import random
import string

# taking the nasty input
length = int(input("Enter the length of the password: "))

# Ensure the length is at least 4 for complexity
if length < 4:
    print("Password length should be at least 4 characters.")
else:
    # Defining the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensuring that ki  the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the remaining length with random choices from all sets
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)
    
    # Shufflingggg !!!
    random.shuffle(password)
    
    # Convert the list to a string and print it
    password_str = ''.join(password)
    print("Generated password:", password_str)
