#!/usr/bin/python3
import itertools

password = "password123" # The actual password

# A list of possible characters to use in the brute-force attack
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

# Using the itertools.product function to generate all possible combinations of characters
for attempt in itertools.product(chars, repeat=8):
    # Joining the characters together to form a string
    attempt_str = ''.join(attempt)
    print(attempt_str)
    if attempt_str == password:
        print("Password found: ", attempt_str)
        break
