#!/usr/bin/python3
import random
import string

def generate_password() -> str:
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            break
        except:
            print("Invalid input. Please enter an integer.")

    valid_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(valid_chars) for i in range(length))
    return password

# Example usage:
password = generate_password()
print("Your password is: ", password)
