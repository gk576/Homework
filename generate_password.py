import random

def generate_password():
    # we define the characters manually
    lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?'

    # then combine all character sets in one string
    all_characters = lower_case_letters + upper_case_letters + digits + special_characters

    # we select 10 random characters from the combined set
    password = random.sample(all_characters, 10)
    
    # join the list into a string and return
    return ''.join(password)

# finally, we generate and print a random password
password = generate_password()
print("Generated password:", password)
